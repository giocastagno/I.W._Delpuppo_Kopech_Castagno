from django import forms
from sitio.models import Itinerario, Dia, Perfil_Usuario, Comentario, Puntaje
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget
from django.forms import BaseModelFormSet

class ItinerarioForm(forms.ModelForm):
    class Meta:
        model = Itinerario
        widgets = {
        	'titulo': forms.Textarea(attrs={'cols': 50, 'rows': 1, 'style':'resize:none;'}),
            'texto_general': SummernoteWidget(attrs={
            	'width': '100%',
        		'height': '300',
				'toolbar': [
			    	['style', ['bold', 'italic', 'underline', 'clear']],
			    	['font', ['strikethrough', 'superscript', 'subscript']],
			    	['fontsize', ['fontsize']],
			    	['color', ['color']],
			    	['para', ['ul', 'ol', 'paragraph']],
			    	['height', ['height']]]
				}),
            'fecha_salida': DateWidget(attrs={'usel10n':'True', 'bootstrap_version':'3'}),
            'fecha_llegada': DateWidget(attrs={'usel10n':'True', 'bootstrap_version':'3'}),
            }
        exclude = ['fecha', 'usuario', 'estado', 'valoracion', 'visitas',]

class DiaForm(forms.ModelForm):
	class Meta:
		model = Dia
		widgets = {
			'descripcion': SummernoteWidget({
        	'height': '150',
			'toolbar': [
			    ['style', ['bold', 'italic', 'underline', 'clear']],
			    ['fontsize', ['fontsize']],
			    ['color', ['color']]]
			}),
		} 
		exclude = ['fecha','usuario','itinerario',]

class PerfilForm(forms.ModelForm):
	class Meta:
		model = Perfil_Usuario 
		exclude = ['usuario',]

class ComentarioForm(forms.ModelForm):
	class Meta:
		model = Comentario
		widgets = {
        	'texto': SummernoteWidget({
        	'height': '150',
			'toolbar': [
			    ['style', ['bold', 'italic', 'underline', 'clear']]]
			}),
        }
		exclude = ['usuario', 'fecha', 'itinerario', 'denuncias',]

class PuntajeForm(forms.ModelForm):
	class Meta:
		model = Puntaje
		exclude = ['usuario', 'itinerario',]




