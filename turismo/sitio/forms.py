from django import forms

from sitio.models import Itinerario, Dia


class ItinerarioForm(forms.ModelForm):
    class Meta:
        model = Itinerario
        exclude = ['fecha', 'usuario', 'estado', ]

class DiaForm(forms.ModelForm):
	class Meta:
		model = Dia 
		exclude = ['fecha','usuario','itinerario',]




