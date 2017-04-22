from django import forms

from sitio.models import Itinerario


class ItinerarioForm(forms.ModelForm):
    class Meta:
        model = Itinerario
        
        exclude = ['fecha', 'usuario', 'estado', ]




