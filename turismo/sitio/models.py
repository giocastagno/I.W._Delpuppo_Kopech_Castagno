from django.contrib import admin
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    foto_perfil = models.ImageField(upload_to = 'sitio/imagenes/', 
        default = 'sitio/imagenes/none/no-img.png')

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
    foto_dia = models.ImageField(upload_to = 'sitio/imagenes/', 
        default = 'sitio/imagenes/none/no-img.png')

    def __str__(self):
        return self.descripcion

class Comentario(models.Model):
    itinerario = models.ForeignKey(Itinerario, null=True, blank=True)
    usuario = models.ForeignKey(User, null=True, blank=True)
    texto = models.CharField(max_length=1000)
    fecha = models.DateTimeField()
    MALO = '1'
    REGULAR = '2'
    BUENO = '3'
    MUY_BUENO = '4'
    EXCELENTE = '5'
    CALIFICACION_CHOICES = (
        (MALO, 'Malo'),
        (REGULAR, 'Regular'),
        (BUENO, 'Bueno'),
        (MUY_BUENO, 'Muy Bueno'),
        (EXCELENTE, 'Excelente'),
    )
    calificacion = models.CharField(
        max_length=1,
        choices=CALIFICACION_CHOICES,
        default='3',
    )

    def __str__(self):
        return self.texto
