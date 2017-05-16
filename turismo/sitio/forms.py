from django import forms

from sitio.models import Itinerario, Dia, Perfil_Usuario, Comentario


class ItinerarioForm(forms.ModelForm):
    class Meta:
        model = Itinerario
        exclude = ['fecha', 'usuario', 'estado', ]

class DiaForm(forms.ModelForm):
	class Meta:
		model = Dia 
		exclude = ['fecha','usuario','itinerario',]

class PerfilForm(forms.ModelForm):
	class Meta:
		model = Perfil_Usuario 
		exclude = ['usuario',]

class ComentarioForm(forms.ModelForm):
	class Meta:
		model = Comentario 
		exclude = ['usuario', 'fecha', 'itinerario',]




