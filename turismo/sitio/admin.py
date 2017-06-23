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

def RestringirItinerario(modeladmin, request, queryset):
	for itinerario in queryset:
		itinerario.estado = "EliminadoLogicamente"
		itinerario.save()
RestringirItinerario.short_description = "Restringir lógicamente los itinerarios seleccionados"

def RestringirComentario(modeladmin, request, queryset):
	for comentario in queryset:
		comentario.estado = "Restringido"
		comentario.save()
RestringirComentario.short_description = "Restringir los comentarios seleccionados"

def RestringirUsuarioDenunciado(modeladmin, request, queryset):
	for denuncia in queryset:
		usuario = User.objects.get(username = denuncia.usuario_denunciado)
		perfil = Perfil_Usuario.objects.get(usuario = usuario)
		perfil.estado = "Restringido"
		perfil.save()
RestringirUsuarioDenunciado.short_description = "Restringir los usuarios seleccionados"

def RestringirItinerarioDenunciado(modeladmin, request, queryset):
	for denuncia in queryset:
		itinerario = denuncia.itinerario
		itinerario.estado = "EliminadoLogicamente"
		itinerario.save()
RestringirItinerarioDenunciado.short_description = "Restringir los itinerarios seleccionados"

def RestringirComentarioDenunciado(modeladmin, request, queryset):
	for denuncia in queryset:
		comentario = denuncia.comentario
		comentario.estado = "Restringido"
		comentario.save()
RestringirComentarioDenunciado.short_description = "Restringir los comentarios seleccionados"

def RestaurarItinerarioRestringido(modeladmin, request, queryset):
	for itinerariodenunciado in queryset:
		itinerario = itinerariodenunciado.itinerario
		itinerario.estado = "Publicado"
		denuncia = ItinerariosDenunciados.objects.get(itinerario = itinerario)
		denuncia.cantidad = 0
		denuncia.save()
		itinerario.save()
RestaurarItinerarioRestringido.short_description = "Restaurar los itinerarios seleccionados"

def RestaurarComentarioRestringido(modeladmin, request, queryset):
	for comentariodenunciado in queryset:
		comentario = comentariodenunciado.comentario
		comentario.estado = "Activo"
		denuncia = ComentariosDenunciados.objects.get(comentario = comentario)
		denuncia.cantidad = 0
		denuncia.save()
		comentario.save()
RestaurarComentarioRestringido.short_description = "Restaurar los comentarios seleccionados"

class AdminItinerario(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'fecha', 'foto_general', 'fecha_salida', 'estado', 'valoracion', 'visitas')
    #list_filter = ('archivada', 'fecha', 'categoria')
    #search_fields = ('texto', )
    date_hierarchy = 'fecha'
    actions = [RestringirItinerario, RestaurarItinerarioRestringido]

class AdminDia(admin.ModelAdmin):
    list_display = ('id', 'itinerario', 'descripcion')

class AdminPerfil(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'nombre', 'apellido', 'estado')   
    actions = [RestringirUsuario, ActivarUsuario]

class AdminComentario(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'texto', 'itinerario', 'estado')  
    actions = [RestringirComentario]
class AdminPuntaje(admin.ModelAdmin):
	list_display = ('id','usuario','itinerario','calificacion')

class AdminItinerariosDenunciados(admin.ModelAdmin):
	list_display = ('id','usuario_denunciado', 'itinerario','cantidad', 'ver_itinerario')
	actions = [RestringirUsuarioDenunciado, RestringirItinerarioDenunciado, RestaurarItinerarioRestringido]
	view_on_site = True
	def ver_itinerario(self, obj):
		url = '/ver_itinerario/'+ str(obj.itinerario.id)
		if not settings.os.environ.get('HEROKU', False):
			return '<a href="http://127.0.0.1:8000%s">Ir</a>' % url
		else:
			return '<a href="https://iwturismo.herokuapp.com%s">Ir</a>' % url
	ver_itinerario.allow_tags = True
	ver_itinerario.short_description = 'Ver itinerario denunciado'
	def get_actions(self, request):
		actions = super(AdminItinerariosDenunciados, self).get_actions(request)
		if 'delete_selected' in actions:
			del actions['delete_selected']
		return actions

class AdminComentariosDenunciados(admin.ModelAdmin):
	list_display = ('id','usuario_denunciado','comentario','cantidad', 'ver_comentario')
	actions = [RestringirUsuarioDenunciado, RestringirComentarioDenunciado, RestaurarComentarioRestringido]
	view_on_site = True
	def ver_comentario(self, obj):
		url = '/ver_itinerario/'+ str(obj.comentario.itinerario.id)
		if not settings.os.environ.get('HEROKU', False):
			return '<a href="http://127.0.0.1:8000%s">Ir</a>' % url
		else:
			return '<a href="https://iwturismo.herokuapp.com%s">Ir</a>' % url
	ver_comentario.allow_tags = True
	ver_comentario.short_description = 'Ver comentario denunciado'
	def get_actions(self, request):
		actions = super(AdminComentariosDenunciados, self).get_actions(request)
		if 'delete_selected' in actions:
			del actions['delete_selected']
		return actions


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
