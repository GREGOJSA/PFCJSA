from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):

    class Meta:
        model = usuarios
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'id_grado',
        ]
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': "Correo electronico",
            'id_grado': "id_grado",
        }

class NuevaEmpresaform(forms.ModelForm):

    class Meta:
        model = empresas
        fields = ['nombre_empresa',
                  'ubicacion',
                  'tutor',
        ]
        labels = {
            'nombre_empresa': 'Nombre de la empresa',
            'ubicacion': 'Ubicacion',
            'tutor': 'Tutor',
        }
