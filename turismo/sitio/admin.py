from django.contrib import admin

from sitio.models import Itinerario, Dia, Perfil_Usuario, Comentario, Puntaje

class AdminItinerario(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'fecha', 'foto_general', 'fecha_salida', 'estado', 'valoracion', 'visitas')
    #list_filter = ('archivada', 'fecha', 'categoria')
    #search_fields = ('texto', )
    date_hierarchy = 'fecha'

class AdminDia(admin.ModelAdmin):
    list_display = ('id', 'itinerario', 'descripcion')

class AdminPerfil(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'nombre', 'apellido', 'estado')   

class AdminComentario(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'texto', 'itinerario')  

class AdminPuntaje(admin.ModelAdmin):
	list_display = ('id','usuario','itinerario','calificacion')


admin.site.register(Itinerario, AdminItinerario)
admin.site.register(Dia, AdminDia)
admin.site.register(Perfil_Usuario, AdminPerfil)
admin.site.register(Comentario, AdminComentario)
admin.site.register(Puntaje, AdminPuntaje)