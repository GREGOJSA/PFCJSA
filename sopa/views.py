from __future__ import unicode_literals
# -- coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic.edit import FormView
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib import auth
from django.views.generic import CreateView
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from formtools.wizard.views import SessionWizardView


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
    return render(request, 'sopa/home.html')


class crearempresa(CreateView):
        model = empresas
        template_name = "sopa/nueva_empresa.html"
        form_class = NuevaEmpresaform
        success_url = reverse_lazy('lista_empresas')

@login_required
def lista_empresas(request):
    empresa = empresas.objects.all()
    return render(request, 'sopa/lista_empresas.html', {'empresas' : empresa})

def miperfil(request):
    usuario = get_object_or_404(usuarios, username = request.user)
    grado = get_object_or_404(grados, id_grado = usuario.id_grado)
    return render(request, 'sopa/perfil_usuario.html', {'usuario' : usuario, 'grado' : grado})

@login_required
def lista_usuarios(request):
    usuario = usuarios.objects.all()
    return render(request, 'sopa/lista_alumnos.html', {'alumnos' : usuario})

@login_required
def detalle_usuario(request, u):
    usuario = get_object_or_404(usuarios, username = u)
    grado = get_object_or_404(grados, id_grado = usuario.id_grado)
    return render(request, 'sopa/detalle_usuario.html', {'usuario' : usuario, 'grado' : grado})

@login_required
def detalle_empresa(request, p):
    empresa = get_object_or_404(empresas, nombre_empresa = p)
    hayopiniones = encuestas.objects.filter(nombre_empresa = p)
    if hayopiniones:
        aux=""
        opiniones = hayopiniones
    else:
        aux="No se han aniadido opiniones"
        opiniones = ""
    return render(request, 'sopa/detalle_empresa.html', {'empresa' : empresa, 'opiniones': opiniones, "aux": aux})

@login_required
def detalle_encuesta(request, pk):
    encuesta = get_object_or_404(encuestas, pk = pk)
    return render(request, 'sopa/detalle_encuesta.html', {'encuesta' : encuesta})

class EncuestaWizard(SessionWizardView):
    template_name = "sopa/cuestionario.html"

    def done(self, form_list, **kwargs):
        print('Encuesta realizada')
        datos={}
        for x in form_list:
            datos=dict(datos.items()+x.cleaned_data.items())
        encuesta = encuestas(
        user = self.request.user,
        nombre_empresa = datos['nombre_empresa'],
        created_date = timezone.now(),
        pf1 = str(datos['pf1']),
        pf11 = str(datos['pf11']),
        pf2 = str(datos['pf2']),
        pf22 = str(datos['pf22']),
        pb1 = str(datos['pb1']),
        pb2 = str(datos['pb2']),
        pb3 = str(datos['pb3']),
        pb4 = str(datos['pb4']),
        ps1 = str(datos['ps1']),
        ps2 = str(datos['ps2']),
        ps3 = str(datos['ps3']),
        ps4 = str(datos['ps3']),
        ps5 = str(datos['ps5']),
        ps6 = str(datos['ps6']),
        ps7 = str(datos['ps7']),
        pa1 = str(datos['pa1']),
        pa2 = str(datos['pa2'])
        )
        encuesta.save()


        return HttpResponseRedirect("/empresas")
