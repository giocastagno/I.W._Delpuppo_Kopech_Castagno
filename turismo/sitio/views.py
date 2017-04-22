from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.models import User
from sitio.models import Itinerario, Estado, Dia, Pais
from sitio.forms import ItinerarioForm
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q


def inicio(request):
    itinerarios = Itinerario.objects.all()
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

def lista_itinerarios_ajax(request):
    itinerarios = Itinerario.objects.order_by('-fecha')[:3]
    return render(request, 'lista_itinerarios.html', {'lista_itinerarios' : itinerarios})

def lista_usuarios_ajax(request):
    usuarios = User.objects.all()
    return render(request, 'lista_usuarios.html', {'lista_usuarios' : usuarios})

def usuarios_online_ajax(request):
    datos = {
        'cantidad_usuarios_online_registrados': User.objects.filter(Q(is_authenticated = True) | Q(is_anonymous = True)).count(),

    }
    return JsonResponse(datos)


