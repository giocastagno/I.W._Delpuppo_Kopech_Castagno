from haystack import indexes
from sitio.models import Itinerario, Comentario, Dia
from django_countries.fields import CountryField

class ItinerarioIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	titulo = indexes.CharField(model_attr='titulo')
	fecha = indexes.DateTimeField(model_attr='fecha')
	pais_destino = indexes.CharField(model_attr='pais_destino')

	def get_model(self):
		return Itinerario

	def index_queryset(self, using=None):
		return self.get_model().objects.filter(estado='Publicado')

class ComentarioIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	texto = indexes.CharField(model_attr='texto')
	fecha = indexes.DateTimeField(model_attr='fecha')
	id_itinerario = indexes.IntegerField(model_attr='itinerario__pk')
	estado = indexes.CharField(model_attr = 'itinerario__estado')
	titulo_itinerario = indexes.CharField(model_attr='itinerario__titulo')
	fecha_itinerario = indexes.DateTimeField(model_attr = 'itinerario__fecha')

	def get_model(self):
		return Comentario

	def index_queryset(self, using=None):
		return self.get_model().objects.all()

class DiaIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	descripcion = indexes.CharField(model_attr='descripcion')
	id_itinerario = indexes.IntegerField(model_attr='itinerario__pk')
	estado = indexes.CharField(model_attr = 'itinerario__estado')
	titulo_itinerario = indexes.CharField(model_attr='itinerario__titulo')
	fecha_itinerario = indexes.DateTimeField(model_attr = 'itinerario__fecha')

	def get_model(self):
		return Dia

	def index_queryset(self, using=None):
		return self.get_model().objects.all()