from django.shortcuts import render, get_object_or_404
#Importamos la vista generica FormView
from django.views.generic.edit import FormView
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
#Importamos el formulario de autenticacion de django
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib import auth
from django.views.generic import CreateView
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required



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
    print(u)
    usuario = get_object_or_404(usuarios, username = u)
    grado = get_object_or_404(grados, id_grado = usuario.id_grado)
    return render(request, 'sopa/detalle_usuario.html', {'usuario' : usuario, 'grado' : grado})
