from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from django import forms
from django_countries.fields import CountryField
from django.conf import settings
import os

class Localidad(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class ManejadorPerfil(models.Manager):
    def crear_perfil(self, idperfil,usuario):
        perfil = self.create(id=idperfil,usuario=usuario)
        return perfil

class ManejadorPuntaje(models.Manager):
    def crear_puntaje(self, usuario, itinerario,vcalificacion):
        puntaje = self.create(usuario=usuario,itinerario=itinerario,calificacion = vcalificacion)
        return puntaje

class Perfil_Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    foto_perfil = models.ImageField(upload_to = 'sitio/imagenes/', 
        default = os.path.join(settings.STATIC_URL,'sitio/imagenes/','turismo_noimagen.jpg'))
    localidad = models.ForeignKey(Localidad, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank = True)
    usuario = models.ForeignKey(User, null=True, blank=True)
    objects = ManejadorPerfil()
    estado = models.CharField(max_length=20, default = "Activo")

    def __str__(self):
        return self.apellido + ', ' + self.nombre

class Itinerario(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True)
    titulo = models.CharField(max_length=50)
    texto_general = models.CharField(max_length=1000)
    foto_general = models.ImageField(upload_to = 'sitio/imagenes/', 
        default = os.path.join(settings.STATIC_URL,'sitio/imagenes/','turismo_noimagen.jpg'))
    pais_destino = CountryField()
    fecha = models.DateTimeField()
    estado = models.CharField(max_length=20, null=True, blank=True)
    valoracion = models.IntegerField(default=0) 
    visitas = models.IntegerField(default=0)
    
    #tiempo viaje (restringir fecha llegada mayor)
    fecha_salida = models.DateField()
    fecha_llegada = models.DateField()

    def __str__(self):
        return self.titulo + '(' + str(self.fecha) + ')'

'''class ContenidoDenunciado(models.Model): 
    usuario = models.ForeignKey(User, null=True, blank=True)
    tipo = models.CharField(max_length=20, null=True, blank=True)'''

class Puntaje(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True)
    itinerario = models.ForeignKey(Itinerario, null=True, blank=True)
    CALIFICACION_CHOICES = (
        (1, 'Malo'),
        (2, 'Regular'),
        (3, 'Bueno'),
        (4, 'Muy Bueno'),
        (5, 'Excelente'),
    )
    calificacion = models.IntegerField(
        choices=CALIFICACION_CHOICES,
        null = True,
        blank = True,
    )
    objects = ManejadorPuntaje()

    def __str__(self):
        return str(self.calificacion)

class Dia(models.Model):
    itinerario = models.ForeignKey(Itinerario, null=True, blank=True)
    descripcion = models.CharField(max_length=1000)
    foto_dia = models.ImageField(upload_to = 'sitio/imagenes/', 
        default = os.path.join(settings.STATIC_URL,'sitio/imagenes/','turismo_noimagen.jpg'))

    def __str__(self):
        return self.descripcion

class Comentario(models.Model):
    itinerario = models.ForeignKey(Itinerario, null=True, blank=True)
    usuario = models.ForeignKey(User, null=True, blank=True)
    texto = models.CharField(max_length=500)
    fecha = models.DateTimeField()

    def __str__(self):
        return self.texto
