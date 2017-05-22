from haystack import indexes
from sitio.models import Itinerario

class ItinerarioIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	titulo = indexes.CharField(model_attr='titulo')
	fecha = indexes.DateTimeField(model_attr='fecha')

	def get_model(self):
		return Itinerario

	def index_queryset(self, using=None)
		return self.get_model().objects.filter(estado='Publicado')