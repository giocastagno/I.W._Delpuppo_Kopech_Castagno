from django.contrib import admin

from sitio.models import Itinerario, Dia, Perfil_Usuario, Comentario, Puntaje, ComentarioDenuncia
from sitio.models import ItinerariosDenunciados, ComentariosDenunciados, ItinerarioDenuncia


def RestringirUsuario(modeladmin, request, queryset):
	for usuario in queryset:
		usuario.estado = "Restringido"
		usuario.save()
RestringirUsuario.short_description = "Restringir los usuarios seleccionados"
def ActivarUsuario(modeladmin, request, queryset):
	for usuario in queryset:
		usuario.estado = "Activo"
		usuario.save()
ActivarUsuario.short_description = "Activar los usuarios seleccionados"
def EliminarLogItinerario(modeladmin, request, queryset):
	for itinerario in queryset:
		itinerario.estado = "EliminadoLogicamente"
		itinerario.save()
EliminarLogItinerario.short_description = "Eliminar lógicamente los itinerarios seleccionados"
def EliminarComentarioDenunciado(modeladmin, request, queryset):
	for comentario in queryset:
		comentario.texto = "Este comentario ha sido eliminado por violar los términos y condiciones de Santa Fe por el mundo"
		comentario.save()
EliminarComentarioDenunciado.short_description = "Eliminar los comentarios denunciados seleccionados"


class AdminItinerario(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'fecha', 'foto_general', 'fecha_salida', 'estado', 'valoracion', 'visitas')
    #list_filter = ('archivada', 'fecha', 'categoria')
    #search_fields = ('texto', )
    date_hierarchy = 'fecha'
    actions = [EliminarLogItinerario]

class AdminDia(admin.ModelAdmin):
    list_display = ('id', 'itinerario', 'descripcion')

class AdminPerfil(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'nombre', 'apellido', 'estado')   
    actions = [RestringirUsuario, ActivarUsuario]

class AdminComentario(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'texto', 'itinerario')  
    actions = [EliminarComentarioDenunciado]
class AdminPuntaje(admin.ModelAdmin):
	list_display = ('id','usuario','itinerario','calificacion')

class AdminItinerariosDenunciados(admin.ModelAdmin):
	list_display = ('id','usuario_denunciado','itinerario','cantidad')
	#def url_itinerario(self, itinerario):
     #   return format_html("<a href='{url}'>{url}</a>", url=obj.firm_url)
class AdminComentariosDenunciados(admin.ModelAdmin):
	list_display = ('id','usuario_denunciado','comentario','cantidad')

#Esto no lo maneja el administrador, solo lo dejamos para control nuestro
class AdminItinerarioDenuncia(admin.ModelAdmin):
	list_display = ('id','usuario_denunciante', 'itinerario')
class AdminComentarioDenuncia(admin.ModelAdmin):
	list_display = ('id','usuario_denunciante', 'comentario')

admin.site.register(Itinerario, AdminItinerario)
admin.site.register(Dia, AdminDia)
admin.site.register(Perfil_Usuario, AdminPerfil)
admin.site.register(Comentario, AdminComentario)
admin.site.register(Puntaje, AdminPuntaje)
admin.site.register(ItinerariosDenunciados, AdminItinerariosDenunciados)
admin.site.register(ComentariosDenunciados, AdminComentariosDenunciados)
admin.site.register(ItinerarioDenuncia, AdminItinerarioDenuncia)
admin.site.register(ComentarioDenuncia, AdminComentarioDenuncia)
