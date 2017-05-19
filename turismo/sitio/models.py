from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from django import forms
from django_countries.fields import CountryField

class Localidad(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class ManejadorPerfil(models.Manager):
    def crear_perfil(self, idperfil,usuario):
        perfil = self.create(id=idperfil,usuario=usuario)
        return perfil

class Perfil_Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    foto_perfil = models.ImageField(upload_to = 'sitio/imagenes/', 
        default = 'sitio/imagenes/none/no-img.png')
    localidad = models.ForeignKey(Localidad, null=True, blank=True)
    telefono = models.CharField(max_length=20)
    usuario = models.ForeignKey(User, null=True, blank=True)
    objects = ManejadorPerfil()

    def __str__(self):
        return self.apellido + ', ' + self.nombre



class Itinerario(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True)
    titulo = models.CharField(max_length=50)
    texto_general = models.CharField(max_length=1000)
    foto_general = models.ImageField(upload_to = 'sitio/imagenes/', 
        default = 'sitio/imagenes/none/no-img.png')
    pais_destino = CountryField()
    fecha = models.DateTimeField()
    estado = models.CharField(max_length=20, null=True, blank=True)
    
    #tiempo viaje (restringir fecha llegada mayor)
    fecha_salida = models.DateField()
    fecha_llegada = models.DateField()

    def __str__(self):
        return self.titulo + '(' + str(self.fecha) + ')'

class Dia(models.Model):
    itinerario = models.ForeignKey(Itinerario, null=True, blank=True)
    descripcion = models.CharField(max_length=1000)
    foto_dia = models.ImageField(upload_to = 'sitio/imagenes/', 
        default = 'sitio/imagenes/none/no-img.png')

    def __str__(self):
        return self.descripcion

class Comentario(models.Model):
    itinerario = models.ForeignKey(Itinerario, null=True, blank=True)
    usuario = models.ForeignKey(User, null=True, blank=True)
    CALIFICACION_CHOICES = (
        ('Malo', 'Malo'),
        ('Regular', 'Regular'),
        ('Bueno', 'Bueno'),
        ('Muy Bueno', 'Muy Bueno'),
        ('Excelente', 'Excelente'),
    )
    calificacion = models.CharField(
        max_length=9,
        choices=CALIFICACION_CHOICES,
        default='3',
    )
    texto = models.CharField(max_length=500)
    fecha = models.DateTimeField()

    def __str__(self):
        return self.texto
