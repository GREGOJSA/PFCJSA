# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class usuarios (AbstractUser):
    # Hereda de la clase user e icorpora el id grado para identifical al titulacion
    id_grado = models.IntegerField(null=True,blank=True,default='0')

class grados (models.Model):
    id_grado = models.IntegerField(null=True,blank=True)
    nombre_grado = models.TextField(null=True,blank=True,default='')

class empresas (models.Model):
    nombre_empresa = models.TextField(max_length=30,null=True,blank=True,default='')
    created_date = models.DateTimeField(default=timezone.now)
    ubicacion = models.TextField(max_length=40,null=True,blank=True,default='')
    tutor = models.TextField(max_length=25,null=True,blank=True,default='')
    departamento = models.TextField(max_length=20,null=True,blank=True,default='')
    valoracion = models.IntegerField(null=True,blank=True,default='0')



class encuestas (models.Model):

    user = models.TextField(max_length=20,null=True,blank=True,default='')
    nombre_empresa = models.TextField(max_length=30,null=True,blank=True,default='')
    tutor = models.TextField(max_length=20,null=True,blank=True,default='')
    departamento = models.TextField(max_length=20,null=True,blank=True,default='')
    id_encuesta = models.IntegerField(null=True,blank=True,default='0')
    created_date = models.DateTimeField(default=timezone.now)
    # Preguntas fundamentales
    pf1 = models.TextField(max_length=20,null=True,blank=True,default='')
    pf11 = models.TextField(max_length=20,null=True,blank=True,default='')
    pf2 = models.TextField(max_length=20,null=True,blank=True,default='')
    pf22 = models.TextField(max_length=20,null=True,blank=True,default='')
    # Preguntas basicas importantes
    pb1 = models.TextField(max_length=20,null=True,blank=True,default='')
    pb2 = models.TextField(max_length=20,null=True,blank=True,default='')
    pb3 = models.TextField(max_length=20,null=True,blank=True,default='')
    pb4 = models.TextField(max_length=20,null=True,blank=True,default='')
    # Preguntas secundarias de menor importancia
    ps1 = models.TextField(max_length=20,null=True,blank=True,default='')
    ps2 = models.TextField(max_length=20,null=True,blank=True,default='')
    ps3 = models.TextField(max_length=20,null=True,blank=True,default='')
    ps4 = models.TextField(max_length=20,null=True,blank=True,default='')
    ps5 = models.TextField(max_length=20,null=True,blank=True,default='')
    ps6 = models.TextField(max_length=20,null=True,blank=True,default='')
    ps7 = models.TextField(max_length=20,null=True,blank=True,default='')
    # Preguntas anecdoticas para completar
    pa1 = models.TextField(max_length=20,null=True,blank=True,default='')
    pa2 = models.TextField(max_length=20,null=True,blank=True,default='')
    nota = models.IntegerField(null=True,blank=True,default='0')
