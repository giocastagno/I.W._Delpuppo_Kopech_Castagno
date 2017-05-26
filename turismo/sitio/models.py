from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from django import forms
from django_countries.fields import CountryField
from django.conf import settings
import os

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
    LOCALIDAD_CHOICES = (
        ('Acebal', 'Acebal'),
        ('Alcorta', 'Alcorta'),
        ('Alejandra', 'Alejandra'),
        ('Álvarez', 'Álvarez'),
        ('Alvear', 'Alvear'),
        ('Arequito', 'Arequito'),
        ('Armstrong', 'Armstrong'),
        ('Arroyo Seco', 'Arroyo Seco'),
        ('Arteaga', 'Arteaga'),
        ('Ataliva','Ataliva'),
        ('Avellaneda', 'Avellaneda'),
        ('Barrancas', 'Barrancas'),
        ('Barrio Arroyo del Medio', 'Barrio Arroyo del Medio'),
        ('Barrio Mitre', 'Barrio Mitre'),
        ('Barrios Acapulco y Veracruz', 'Barrios Acapulco y Veracruz'),
        ('Berabevú', 'Berabevú'),
        ('Bigand', 'Bigand'),
        ('Bombal', 'Bombal'),
        ('Calchaquí', 'Calchaquí'),
        ('Capitán Bermúdez', 'Capitán Bermúdez'),
        ('Carcarañá', 'Carcarañá'),
        ('Carlos Pellegrini', 'Carlos Pellegrini'),
        ('Casilda', 'Casilda'),
        ('Cayastá', 'Cayastá'),
        ('Cañada Rosquín', 'Cañada Rosquín'),
        ('Cañada de Gómez', 'Cañada de Gómez'),
        ('Centeno', 'Centeno'),
        ('Ceres', 'Ceres'),
        ('Chabás', 'Chabás'),
        ('Chovet', 'Chovet'),
        ('Coronda', 'Coronda'),
        ('Correa', 'Correa'),
        ('El Trébol', 'El Trébol'),
        ('Elortondo', 'Elortondo'),
        ('Empalme Villa Constitución', 'Empalme Villa Constitución'),
        ('Esperanza', 'Esperanza'),
        ('Estación Clucellas', 'Estación Clucellas'),
        ('Fighiera', 'Fighiera'),
        ('Firmat', 'Firmat'),
        ('Florencia', 'Florencia'),
        ('Franck', 'Franck'),
        ('Frontera', 'Frontera'),
        ('Fuentes', 'Fuentes'),
        ('General Lagos', 'General Lagos'),
        ('Gobernador Crespo', 'Gobernador Crespo'),
        ('Gálvez', 'Gálvez'),
        ('Colonia Hansen', 'Colonia Hansen'),
        ('Helvecia', 'Helvecia'),
        ('Hersilia', 'Hersilia'),
        ('Hughes', 'Hughes'),
        ('Humberto Primo','Humberto Primo'),
        ('Humboldt', 'Humboldt'),
        ('Ibarlucea', 'Ibarlucea'),
        ('Juan de Garay', 'Juan de Garay'),
        ('La Gallareta', 'La Gallareta'),
        ('Laguna Paiva', 'Laguna Paiva'),
        ('Las Parejas', 'Las Parejas'),
        ('Las Rosas', 'Las Rosas'),
        ('Las Toscas', 'Las Toscas'),
        ('Lehmann', 'Lehmann'),
        ('Llambi Campbell', 'Llambi Campbell'),
        ('Los Quirquinchos', 'Los Quirquinchos'),
        ('Maciel', 'Maciel'),
        ('Malabrigo', 'Malabrigo'),
        ('Margarita', 'Margarita'),
        ('María Juana', 'María Juana'),
        ('María Susana', 'María Susana'),
        ('María Teresa', 'María Teresa'),
        ('Melincué', 'Melincué'),
        ('Moisés Ville', 'Moisés Ville'),
        ('Monte Oscuridad', 'Monte Oscuridad'),
        ('Monte Vera', 'Monte Vera'),
        ('Montes de Oca', 'Montes de Oca'),
        ('Murphy', 'Murphy'),
        ('Máximo Paz', 'Máximo Paz'),
        ('Nelson', 'Nelson'),
        ('Oliveros', 'Oliveros'),
        ('Paraná', 'Paraná'),
        ('Peyrano', 'Peyrano'),
        ('Piamonte', 'Piamonte'),
        ('Pilar', 'Pilar'),
        ('Progreso', 'Progreso'),
        ('Pueblo Esther', 'Pueblo Esther'),
        ('Puerto Gaboto', 'Puerto Gaboto'),
        ('Pujato', 'Pujato'),
        ('Rafaela','Rafaela'),
        ('Reconquista','Reconquista'),
        ('Ricardone', 'Ricardone'),
        ('Rivadavia', 'Rivadavia'),
        ('Romang', 'Romang'),
        ('Rosario','Rosario'),
        ('Rufino', 'Rufino'),
        ('San Antonio de Obligado', 'San Antonio de Obligado'),
        ('San Carlos Centro', 'San Carlos Centro'),
        ('San Carlos Sud', 'San Carlos Sud'),
        ('San Cristóbal','San Cristóbal'),
        ('San Genaro', 'San Genaro'),
        ('San Genaro Norte', 'San Genaro Norte'),
        ('San Gregorio', 'San Gregorio'),
        ('San Guillermo', 'San Guillermo'),
        ('San Javier', 'San Javier'),
        ('San Jerónimo Norte', 'San Jerónimo Norte'),
        ('San Jerónimo Sud', 'San Jerónimo Sud'),
        ('San Jorge', 'San Jorge'),
        ('San José de la Esquina', 'San José de la Esquina'),
        ('San Justo', 'San Justo'),
        ('San Martín de las Escobas', 'San Martín de las Escobas'),
        ('San Vicente', 'San Vicente'),
        ('Sancti Spiritu', 'Sancti Spiritu'),
        ('Santa Clara de Buena Vista', 'Santa Clara de Buena Vista'),
        ('Santa Clara de Saguier', 'Santa Clara de Saguier'),
        ('Santa Emilia', 'Santa Emilia'),
        ('Santa Fe', 'Santa Fe'),
        ('Santa Isabel', 'Santa Isabel'),
        ('Santa María Norte', 'Santa María Norte'),
        ('Santa Rosa de Calchines', 'Santa Rosa de Calchines'),
        ('Santa Teresa', 'Santa Teresa'),
        ('Sastre y Ortiz', 'Sastre y Ortiz'),
        ('Serodino', 'Serodino'),
        ('Soutomayor', 'Soutomayor'),
        ('Suardi', 'Suardi'),
        ('Sunchales','Sunchales'),
        ('Tacuarendí', 'Tacuarendí'),
        ('Teodelina', 'Teodelina'),
        ('Timbúes', 'Timbúes'),
        ('Tortugas', 'Tortugas'),
        ('Tostado', 'Tostado'),
        ('Totoras', 'Totoras'),
        ('Venado Tuerto','Venado Tuerto'),
        ('Vera', 'Vera'),
        ('Vicente Echeverría', 'Vicente Echeverría'),
        ('Videla', 'Videla'),
        ('Villa Cañás', 'Villa Cañás'),
        ('Villa Constitución','Villa Constitución'),
        ('Villa Eloísa', 'Villa Eloísa'),
        ('Villa Guillermina', 'Villa Guillermina'),
        ('Villa Minetti', 'Villa Minetti'),
        ('Villa Mugueta', 'Villa Mugueta'),
        ('Villa Ocampo', 'Villa Ocampo'),
        ('Villa Trinidad', 'Villa Trinidad'),
        ('Wheelwright', 'Wheelwright'),
        ('Zavalla', 'Zavalla'),
    )
    localidad = models.CharField(choices = LOCALIDAD_CHOICES, max_length = 100)
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
