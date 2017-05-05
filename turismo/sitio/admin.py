from django.contrib import admin

from sitio.models import Itinerario, Pais, Estado, Dia, Perfil_Usuario #aca se importan modelos de models.py (crearlos ahi)


class AdminItinerario(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'fecha', 'foto_general')
    #list_filter = ('archivada', 'fecha', 'categoria')
    #search_fields = ('texto', )
    date_hierarchy = 'fecha'

class AdminPais(admin.ModelAdmin):
    list_display = ('id', 'nombre')

class AdminEstado(admin.ModelAdmin):
    list_display = ('id', 'descripcion')

class AdminDia(admin.ModelAdmin):
    list_display = ('id', 'itinerario', 'descripcion')

class AdminPerfil(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'nombre', 'apellido')   


admin.site.register(Itinerario, AdminItinerario)
admin.site.register(Pais, AdminPais)
admin.site.register(Estado, AdminEstado)
admin.site.register(Dia, AdminDia)
admin.site.register(Perfil_Usuario, AdminPerfil)