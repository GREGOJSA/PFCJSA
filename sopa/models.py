from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class usuarios (models.Model):
    user = models.TextField(max_length=15,null=True,blank=True,default='No configurado')
    nombre = models.TextField(max_length=15,null=True,blank=True,default='')
    apellido = models.TextField(max_length=15,null=True,blank=True,default='')
    id_grado = models.IntegerField(null=True,blank=True,default='0')

class grados (models.Model):
    id_grado = models.IntegerField(null=True,blank=True)
    nombre_grado = models.TextField(null=True,blank=True,default='')

class empresas (models.Model):
    nombre_empresa = models.TextField(max_length=30,null=True,blank=True,default='')
    ubicacion = models.TextField(max_length=40,null=True,blank=True,default='')
    tutor = models.TextField(max_length=25,null=True,blank=True,default='')
    valoracion = models.IntegerField(null=True,blank=True,default='0')

class opiniones (models.Model):
    user = models.TextField(max_length=20,null=True,blank=True,default='')
    nombre_empresa = models.TextField(max_length=30,null=True,blank=True,default='')
    id_encuesta = models.IntegerField(null=True,blank=True,default='0')

class encuentas (models.Model):
    id_encuesta = models.IntegerField(null=True,blank=True,default='0')
    p1 = models.TextField(null=True,blank=True,default='')
    p2 = models.TextField(null=True,blank=True,default='')
    p3 = models.TextField(null=True,blank=True,default='')
    p4 = models.TextField(null=True,blank=True,default='')
    p5 = models.TextField(null=True,blank=True,default='')
    p6 = models.TextField(null=True,blank=True,default='')
