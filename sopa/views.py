from django.shortcuts import render
#Importamos la vista generica FormView
from django.views.generic.edit import FormView
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
#Importamos el formulario de autenticacion de django
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

# Create your views here.
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

def home(request):
    if request.user.is_authenticated():
        return render(request, 'sopa/index.html')
    else:
        return HttpResponseRedirect("localhost:9000")
