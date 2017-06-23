from __future__ import unicode_literals
# -- coding: utf-8
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

class PreguntasFundamentalesForm(forms.Form):
        nombre_empresa = forms.CharField(label = 'Nombre de la empresa')

        OpcionesPf1 = (
            ('Programacion Web','Programacion web'),
            ('Redes','Redes'),
            ('Big Data','Big Data'),
            ('Programacion de escritorio','Programacion de escritorio'),
            ('Gestion','Gestion'),
            ('Economia','Economia'),
            ('Eloectronica','Electronica'),
        )
        pf1 = forms.MultipleChoiceField(label = 'Tematicas',
                                        widget = forms.CheckboxSelectMultiple,
                                        choices=OpcionesPf1
                                        )

        pf11 = forms.CharField(label = 'Otras tematicas')

        OpcionesPf2 = (
            ('Transporte','Transporte'),
            ('Economica','Economica'),
            ('Bono comida','Bono comida'),
            ('Ninguna','Ninguna'),
        )

        pf2 = forms.MultipleChoiceField(label = 'Ayudas',
                                        widget = forms.CheckboxSelectMultiple,
                                        choices=OpcionesPf2
                                        )
        pf22 = forms.CharField(label = 'Otras ayudas')




class PreguntasBasicasForm(forms.Form):



        OpcionesPb1 = [('Si','Si'),('No','No')]
        pb1 = forms.ChoiceField(label = 'Practicas remuneradas',
                               choices = OpcionesPb1,
                               widget = forms.RadioSelect(),
                               required=False)

        OpcionesPb2 = [('Si','Si'),('No','No'),('Tal vez','Tal vez')]
        pb2 = forms.ChoiceField(label = 'Posibilidad de posterior contratacion',
                               choices = OpcionesPb2,
                               widget = forms.RadioSelect(),
                               required=False)

        OpcionesPb3=  [('Malo','Malo'),('Normal','Normal'),('Bueno','Bueno')]
        pb3 = forms.ChoiceField(label = 'Relacion personal y laboral con el tutor',
                               choices = OpcionesPb3,
                               widget = forms.RadioSelect(),
                               required=False)

        pb4 = forms.CharField(label = 'Requisitos previos',
                              required=False)

class PreguntasOpcionalesForm(forms.Form):

        OpcionesPs1=  [('Grupal','Grupal'),('Individual','Individual')]
        ps1 = forms.ChoiceField(label = 'Forma de trabajo',
                               choices = OpcionesPs1,
                               widget = forms.RadioSelect(),
                               required=False)

        OpcionesPs2 = [('Jornada completa (40h)','Jornada completa (40h)'),
                     ('Media jornada (20h)','Media jornada (20h)'),
                     ('Jornada intensiva (35h)','Jornada intensiva (35h)')]
        ps2 = forms.ChoiceField(label = 'Tipo de jornada',
                               choices = OpcionesPs2,
                               widget = forms.RadioSelect(),
                               required=False)

        OpcionesPs3 = [('Si','Si'),('No','No')]
        ps3 = forms.ChoiceField(label = 'Flexibilidad de la jornada',
                               choices = OpcionesPs3,
                               widget = forms.RadioSelect(),
                               required=False)

        OpcionesPs4 = [('Si','Si'),('No','No')]
        ps4 = forms.ChoiceField(label = 'Periodo Vacacional',
                               choices = OpcionesPs4,
                               widget = forms.RadioSelect(),
                               required=False)

        OpcionesPs5 = [('6 meses','6 meses'),('3 meses','3 meses')]
        ps5 = forms.ChoiceField(label = 'Duracion de la beca',
                               choices = OpcionesPs5,
                               widget = forms.RadioSelect(),
                               required=False)

        OpcionesPs6 = [('Malo','Malo'),('Normal','Normal'),('Bueno','Bueno')]
        ps6 = forms.ChoiceField(label = 'Ambiente laboral',
                               choices = OpcionesPs6,
                               widget = forms.RadioSelect(),
                               required=False)

        ps7 = forms.CharField(label = 'Descripcion breve del contenido de la beca',
                               required=False)

class PreguntasAnecdoticasForm(forms.Form):

        pa1 = forms.CharField(label = 'Conocimientos adquiridos que anadiras a tu CV',
                               required=False)
        pa2 = forms.CharField(label = 'Comentarios y recomendaciones adicionales',
                               required=False)
