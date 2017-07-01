# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic.edit import FormView
from django.http.response import HttpResponseRedirect, HttpResponseNotFound
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib import auth
from django.views.generic import CreateView
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from formtools.wizard.views import SessionWizardView
import django.utils.encoding
from django.core.exceptions import *
import re

TEMPLATES = {"cuestionario", "sopa/cuestionario.html"}

class Login(FormView):
    #Establecemos la plantilla a utilizar
    template_name = 'sopa/login.html'
    #Le indicamos que el formulario a utilizar es el formulario de autenticacion de Django
    form_class = AuthenticationForm
    #Le decimos que cuando se haya completado exitosamente la operacion nos redireccione a la url bienvenida de la aplicacion personas
    success_url =  reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):
        #Si el usuario esta autenticado entonces nos direcciona a la url establecida en success_url
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.get_success_url())
        #Sino lo esta entonces nos muestra la plantilla del login simplemente
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

class RegistroUsuario(CreateView):
    model = usuarios
    template_name = "sopa/registro.html"
    form_class = RegistroForm
    success_url = reverse_lazy("login")
    def form_valid(self, form, *args, **kwargs):
        response = super(RegistroUsuario, self).form_valid(form, *args, **kwargs)
        user = self.object
        return response


def home(request):
    empresa = empresas.objects.all().order_by('-created_date')[:5]
    opinion = encuestas.objects.all().order_by('-created_date')[:5]
    usuario = usuarios.objects.all().order_by('-date_joined')[:5]
    return render(request, 'sopa/home.html',{'titulo': 'Bienvenido a SOPA','empresas' : empresa, 'opiniones' : opinion, 'usuarios' : usuario})


class crearempresa(CreateView):
        model = empresas
        template_name = "sopa/nueva_empresa.html"
        form_class = NuevaEmpresaform
        success_url = reverse_lazy('lista_empresas')

def notamedia(e):
    emp = encuestas.objects.filter(nombre_empresa = e.nombre_empresa, departamento = e.departamento, tutor = e.tutor)
    nemp = encuestas.objects.filter(nombre_empresa = e.nombre_empresa, departamento = e.departamento, tutor = e.tutor).count()
    a = 0
    if nemp != 0:
        for x in emp:
            a = a + int(x.nota)
        media = a / nemp
        print ('obtenida media de '+x.nombre_empresa)
        print ('media '+ str(media))
        print ('suma puntuaciones ' + str(a))
        print ('numero de encuestas '+ str(nemp))
        empresas.objects.filter(nombre_empresa = e.nombre_empresa, departamento = e.departamento, tutor = e.tutor).update(valoracion = media)
    else:
        print ('no hay opiniones')
        media = 0
        empresas.objects.filter(nombre_empresa = e.nombre_empresa, departamento = e.departamento, tutor = e.tutor).update(valoracion = media)



@login_required
def lista_empresas(request):
    empresa = empresas.objects.all().order_by('nombre_empresa')
    for x in empresa:
        notamedia(x)
    return render(request, 'sopa/lista_empresas.html', {'titulo': 'SOPA lista empresas' ,'empresas' : empresa})

@login_required
def miperfil(request):
    usuario = get_object_or_404(usuarios, username = request.user)
    try:
        grado = grados.objects.get(id_grado=usuario.id_grado)
    except ObjectDoesNotExist:
        grado = "no especificado"
    op = encuestas.objects.filter(user = usuario.username).order_by('created_date')
    if op:
        aux=""
        opiniones = op
    else:
        aux="No he añadido opiniones"
        opiniones = ""
    return render(request, 'sopa/perfil_usuario.html', {'titulo': 'SOPA Mi perfil' ,'usuario' : usuario, 'grado' : grado, 'opinion' : opiniones, 'aux' : aux})

@login_required
def lista_usuarios(request):
    usuario = usuarios.objects.all()
    return render(request, 'sopa/lista_alumnos.html', {'titulo': 'SOPA lista usuarios' ,'alumnos' : usuario})

@login_required
def detalle_usuario(request, u):
    usuario = get_object_or_404(usuarios, username = u)
    try:
        grado = grados.objects.get(id_grado=usuario.id_grado)
    except ObjectDoesNotExist:
        grado = "no especificado"
    hayopiniones = encuestas.objects.filter(user = usuario)
    if hayopiniones:
        aux=""
        opiniones = hayopiniones
    else:
        aux="No ha añadido opiniones"
        opiniones = ""
    return render(request, 'sopa/detalle_usuario.html', {'titulo': 'Detalle de usuario' ,'usuario' : usuario, 'grado' : grado, 'opiniones' : opiniones, 'aux':aux})

@login_required
def detalle_empresa(request, pk):
    empresa = get_object_or_404(empresas, pk = pk)
    hayopiniones = encuestas.objects.filter(nombre_empresa = empresa.nombre_empresa, departamento = empresa.departamento, tutor = empresa.tutor)
    notamedia(empresa)
    if hayopiniones:
        aux=""
        opiniones = hayopiniones
    else:
        aux="No se han añadido opiniones"
        opiniones = ""
    return render(request, 'sopa/detalle_empresa.html', {'titulo': 'SOPA Detalle de empresa' ,'empresa' : empresa, 'opiniones': opiniones, 'aux': aux})

@login_required
def lista_encuestas(request):
    encuesta = encuestas.objects.all().order_by('created_date')
    return render(request, 'sopa/lista_encuestas.html', {'titulo': 'SOPA Encuestas' ,'encuestas' : encuesta})



@login_required
def detalle_encuesta(request, pk):
    encuesta = get_object_or_404(encuestas, pk = pk)
    return render(request, 'sopa/detalle_encuesta.html', {'titulo': 'SOPA Detalle encuesta' ,'encuesta' : encuesta})

@login_required
def eliminar_encuesta(request, pk):
    encuesta = encuestas.objects.get(pk = pk)
    print (request.user)
    print (encuesta.user)
    if str(request.user) == str(encuesta.user):
        encuesta.delete()
        return redirect('/usuarios/miperfil')
    else:
        return HttpResponseNotFound()

def ayuda(request):
    titulo = "SOPA. Ayuda"
    return render(request,'sopa/ayuda.html', {'titulo': 'SOPA Ayuda'})

class EncuestaWizard(SessionWizardView):
    template_name = "sopa/cuestionario.html"

    def done(self, form_list, **kwargs):
        print('Encuesta realizada')
        datos={}
        for x in form_list:
            datos=dict(datos.items()+x.cleaned_data.items())
        a = re.sub("[u']",'',str(datos['pf1']))
        pf1str = a[1:-1]
        b = re.sub("[u']",'',str(datos['pf2']))
        pf2str = b[1:-1]
        encuesta = encuestas(
        user = self.request.user,
        nombre_empresa = self.kwargs.get('e', None),
        departamento = self.kwargs.get('d', None),
        tutor = self.kwargs.get('t', None),
        created_date = timezone.now(),
        pf1 = pf1str,
        pf11 = datos['pf11'],
        pf2 = pf2str,
        pf22 = datos['pf22'],
        pb1 = datos['pb1'],
        pb2 = datos['pb2'],
        pb3 = datos['pb3'],
        pb4 = datos['pb4'],
        ps1 = datos['ps1'],
        ps2 = datos['ps2'],
        ps3 = datos['ps3'],
        ps4 = datos['ps3'],
        ps5 = datos['ps5'],
        ps6 = datos['ps6'],
        ps7 = datos['ps7'],
        pa1 = datos['pa1'],
        pa2 = datos['pa2'],
        nota = datos['nota']
        )
        encuesta.save()


        return HttpResponseRedirect("/empresas/")
