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

class PreguntasBasicasForm(forms.Form):

        nombre_empresa = forms.CharField(label = 'Nombre de la empresa')

        OPCIONESP1=[('Si','Si'),('No','No')]
        pb1 = forms.ChoiceField(label = 'Practicas remuneradas',
                               choices = OPCIONESP1,
                               widget = forms.RadioSelect())
        OPCIONESP2=[('Si','Si'),('No','No'),('Tal vez','Tal vez')]
        pb2 = forms.ChoiceField(label = 'Posibilidad de posterior contratacion',
                               choices = OPCIONESP2,
                               widget = forms.RadioSelect())
        OPCIONESP3=[('Malo','Malo'),('Normal','Normal'),('Bueno','Bueno')]
        pb3 = forms.ChoiceField(label = 'Relacion personal y laboral con el tutor',
                               choices = OPCIONESP3,
                               widget = forms.RadioSelect())

        pb4 = forms.CharField(label = 'Requisitos previos')

class PreguntasOpcionalesForm(forms.Form):
        pregunta4 = forms.CharField()
        pregunta5 = forms.CharField()
        pregunta6 = forms.CharField()
