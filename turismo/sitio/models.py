from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User

class Pais(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Estado(models.Model):
    descripcion = models.CharField(max_length=20)

    def __str__(self):
        return self.descripcion 

class Itinerario(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True)
    titulo = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, null=True, blank=True)
    texto_general = models.CharField(max_length=1000)
    foto_general = models.ImageField(upload_to = 'sitio/imagenes/', 
        default = 'sitio/imagenes/none/no-img.png')
    pais_destino = models.ForeignKey(Pais, null=True, blank=True)
    fecha = models.DateTimeField()
    
    #tiempo viaje (restringir fecha llegada mayor)
    fecha_salida = models.DateField()
    fecha_llegada = models.DateField()

    def __str__(self):
        return self.titulo + '(' + str(self.fecha) + ')'

class Dia(models.Model):
    itinerario = models.ForeignKey(Itinerario, null=True, blank=True)
    descripcion = models.CharField(max_length=1000)

    def __str__(self):
        return self.descripcion