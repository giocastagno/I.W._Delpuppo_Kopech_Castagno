from django.contrib import admin

from sitio.models import Itinerario, Dia, Perfil_Usuario, Comentario, Puntaje, ComentarioDenuncia, User
from sitio.models import ItinerariosDenunciados, ComentariosDenunciados, ItinerarioDenuncia
from turismo import settings


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

def EliminarComentario(modeladmin, request, queryset):
	for comentario in queryset:
		comentario.texto = "Este comentario ha sido eliminado por violar los términos y condiciones de Santa Fe por el mundo"
		comentario.save()
EliminarComentario.short_description = "Eliminar los comentarios seleccionados"

def RestringirUsuarioDenunciado(modeladmin, request, queryset):
	for denuncia in queryset:
		usuario = User.objects.get(username = denuncia.usuario_denunciado)
		perfil = Perfil_Usuario.objects.get(usuario = usuario)
		perfil.estado = "Restringido"
		perfil.save()
RestringirUsuarioDenunciado.short_description = "Restringir los usuarios seleccionados"

def EliminarLogItinerarioDenunciado(modeladmin, request, queryset):
	for denuncia in queryset:
		itinerario = denuncia.itinerario
		itinerario.estado = "EliminadoLogicamente"
		itinerario.save()
EliminarLogItinerarioDenunciado.short_description = "Eliminar lógicamente los itinerarios seleccionados"

def EliminarLogComentarioDenunciado(modeladmin, request, queryset):
	for denuncia in queryset:
		comentario = denuncia.comentario
		comentario.texto = "Este comentario ha sido eliminado por violar los términos y condiciones de Santa Fe por el mundo"
		comentario.save()
EliminarLogComentarioDenunciado.short_description = "Eliminar los comentarios seleccionados"

def RestaurarItinerarioEliminado(modeladmin, request, queryset):
	for itinerario in queryset:
		itinerario.estado = "Publicado"
		itinerario.save()
RestaurarItinerarioEliminado.short_description = "Restaurar los itinerarios seleccionados"

class AdminItinerario(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'fecha', 'foto_general', 'fecha_salida', 'estado', 'valoracion', 'visitas')
    #list_filter = ('archivada', 'fecha', 'categoria')
    #search_fields = ('texto', )
    date_hierarchy = 'fecha'
    actions = [EliminarLogItinerario, RestaurarItinerarioEliminado]

class AdminDia(admin.ModelAdmin):
    list_display = ('id', 'itinerario', 'descripcion')

class AdminPerfil(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'nombre', 'apellido', 'estado')   
    actions = [RestringirUsuario, ActivarUsuario]

class AdminComentario(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'texto', 'itinerario')  
    actions = [EliminarComentario]
class AdminPuntaje(admin.ModelAdmin):
	list_display = ('id','usuario','itinerario','calificacion')

class AdminItinerariosDenunciados(admin.ModelAdmin):
	list_display = ('id','usuario_denunciado','itinerario','cantidad','view_on_site')
	actions = [RestringirUsuarioDenunciado, EliminarLogItinerarioDenunciado]
	view_on_site = True
	def view_on_site(self, obj):
		url = '/ver_itinerario/'+ str(obj.itinerario.id)
		if not settings.os.environ.get('HEROKU', False):
			return '<a href="http://127.0.0.1:8000%s">Ver Itinerario</a>' % url
		else:
			return '<a href="https://iwturismo.herokuapp.com%s">Ver Itinerario</a>' % url
	view_on_site.allow_tags = True

class AdminComentariosDenunciados(admin.ModelAdmin):
	list_display = ('id','usuario_denunciado','comentario','cantidad')
	actions = [RestringirUsuarioDenunciado, EliminarLogComentarioDenunciado]
	list_display_links = ('usuario_denunciado', 'comentario')
	view_on_site = True


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
