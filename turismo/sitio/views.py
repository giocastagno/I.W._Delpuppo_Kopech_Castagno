from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.models import User
from sitio.models import Itinerario
from sitio.forms import ItinerarioForm
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def inicio(request):
    itinerarios = Itinerario.objects.all()[:3]
    return render(request, 'inicio.html', {'lista_itinerarios': itinerarios})

def usuario(request):
    usuarios = User.objects.all()
    return render(request, 'usuario.html', {'lista_usuarios': usuarios})

@login_required
def crear_itinerario(request):
    if request.method == 'POST':
        itinerario_form = ItinerarioForm(request.POST)
        if itinerario_form.is_valid():
            itinerario = itinerario_form.save(commit=False)
            itinerario.fecha = datetime.now()
            itinerario.save()
            return redirect('/inicio/')
    else:
        itinerario_form = ItinerarioForm()

    return render(request, 'crear_itinerario.html', {'form': itinerario_form})


