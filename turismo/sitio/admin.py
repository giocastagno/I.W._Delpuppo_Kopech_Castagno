from django.contrib import admin

from sitio.models import Itinerario, Pais, Dia, Perfil_Usuario, Comentario 

class AdminItinerario(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'fecha', 'foto_general')
    #list_filter = ('archivada', 'fecha', 'categoria')
    #search_fields = ('texto', )
    date_hierarchy = 'fecha'

class AdminPais(admin.ModelAdmin):
    list_display = ('id', 'nombre')

class AdminDia(admin.ModelAdmin):
    list_display = ('id', 'itinerario', 'descripcion')

class AdminPerfil(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'nombre', 'apellido')   

class AdminComentario(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'calificacion', 'texto', 'itinerario')  


admin.site.register(Itinerario, AdminItinerario)
admin.site.register(Pais, AdminPais)
admin.site.register(Dia, AdminDia)
admin.site.register(Perfil_Usuario, AdminPerfil)
admin.site.register(Comentario, AdminComentario)