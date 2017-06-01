from django import forms
from sitio.models import Itinerario, Dia, Perfil_Usuario, Comentario, Puntaje
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget
from django.forms.formsets import BaseFormSet

class BaseDiaFormSet(BaseFormSet):
    def clean(self):
        if any(self.errors):
            return
        for form in self.forms:
            if form.cleaned_data:
                descripcion = form.cleaned_data['descripcion']
                # Check that all links have both an anchor and URL
                if not descripcion:
                    raise forms.ValidationError(
                        'Debe ingresar una descripción',
                        code='falta_descripcion'
                    )

class ItinerarioForm(forms.ModelForm):
    class Meta:
        model = Itinerario
        widgets = {
        	'titulo': forms.Textarea(attrs={'cols': 82, 'rows': 1, 'style':'resize:none;'}),
            'texto_general': SummernoteInplaceWidget(),
            'fecha_salida': DateWidget(attrs={'usel10n':'True', 'bootstrap_version':'3'}),
            'fecha_llegada': DateWidget(attrs={'usel10n':'True', 'bootstrap_version':'3'}),
            	}
        exclude = ['fecha', 'usuario', 'estado', 'valoracion', 'visitas',]

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
		widgets = {
        	'texto': SummernoteInplaceWidget(),
            	}
		exclude = ['usuario', 'fecha', 'itinerario', 'denuncias',]

class PuntajeForm(forms.ModelForm):
	class Meta:
		model = Puntaje
		exclude = ['usuario', 'itinerario',]




