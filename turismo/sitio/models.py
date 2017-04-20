from django.contrib import admin
from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Itinerario(models.Model):
    titulo = models.CharField(max_length=50)
    texto_general = models.CharField(max_length=1000)
    foto_general = models.ImageField(upload_to = 'sitio/imagenes/', default = 'sitio/imagenes/none/no-img.png')
    pais_destino = models.ForeignKey(Pais, null=True, blank=True)
    fecha = models.DateTimeField()


    def __str__(self):
        return self.titulo + '(' + str(self.fecha) + ')'