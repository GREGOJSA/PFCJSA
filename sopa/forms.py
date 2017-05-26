from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class LoginForm(UserCreationForm):

    class Meta:
        model = usuarios
        fields = [
                  'username',
                  'password',
        ]
        labels = {
                  'username' : 'Nombre de usuario',
                  'password' : 'Contraseña',
        }
