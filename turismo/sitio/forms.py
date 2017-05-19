from django import forms
from sitio.models import Itinerario, Dia, Perfil_Usuario, Comentario
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget


class ItinerarioForm(forms.ModelForm):
    class Meta:
        model = Itinerario
        widgets = {
        	'titulo': forms.Textarea(attrs={'cols': 82, 'rows': 1, 'style':'resize:none;'}),
            'texto_general': SummernoteInplaceWidget(),
            'fecha_salida': DateWidget(attrs={'usel10n':'True', 'bootstrap_version':'3'}),
            'fecha_llegada': DateWidget(attrs={'usel10n':'True', 'bootstrap_version':'3'}),
            	}
        exclude = ['fecha', 'usuario', 'estado',]

class DiaForm(forms.ModelForm):
	class Meta:
		model = Dia
		widgets = {
			'descripcion': SummernoteInplaceWidget(),
			} 
		exclude = ['fecha','usuario','itinerario',]

class PerfilForm(forms.ModelForm):
	class Meta:
		model = Perfil_Usuario 
		exclude = ['usuario',]

class ComentarioForm(forms.ModelForm):
	class Meta:
		model = Comentario 
		exclude = ['usuario', 'fecha', 'itinerario',]




