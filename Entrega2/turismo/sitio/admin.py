from django.contrib import admin

from sitio.models import Itinerario #aca se importan modelos de models.py (crearlos ahi)


class AdminItinerario(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'fecha',)
    #list_filter = ('archivada', 'fecha', 'categoria')
    #search_fields = ('texto', )
    date_hierarchy = 'fecha'

admin.site.register(Itinerario, AdminItinerario)
#admin.site.register(Categoria)
