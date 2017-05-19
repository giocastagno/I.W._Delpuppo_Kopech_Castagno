from django.contrib import admin

from sitio.models import Itinerario, Dia, Perfil_Usuario, Comentario 

class AdminItinerario(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'fecha', 'foto_general', 'fecha_salida')
    #list_filter = ('archivada', 'fecha', 'categoria')
    #search_fields = ('texto', )
    date_hierarchy = 'fecha'

class AdminDia(admin.ModelAdmin):
    list_display = ('id', 'itinerario', 'descripcion')

class AdminPerfil(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'nombre', 'apellido')   

class AdminComentario(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'calificacion', 'texto', 'itinerario')  


admin.site.register(Itinerario, AdminItinerario)
admin.site.register(Dia, AdminDia)
admin.site.register(Perfil_Usuario, AdminPerfil)
admin.site.register(Comentario, AdminComentario)