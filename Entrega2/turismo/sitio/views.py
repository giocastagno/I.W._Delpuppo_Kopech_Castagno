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
    nuevo = Itinerario()
    nuevo.titulo = 'Bienvenido al sitio!'
    #nuevo.texto = 'acaba de entrar alguien al sitio'
    nuevo.fecha = datetime.now()
    nuevo.save()

    itinerarios = Itinerario.objects.all()[:3]

    return render(request, 'inicio.html', {'lista_itinerarios': itinerarios})

def usuario(request):
    usuarios = User.objects.all()
    return render(request, 'usuario.html', {'lista_usuarios': usuarios})

def cerrar_sesion(request):
    logout(request)
    return redirect('/accounts/logout/')

def acceso(request):
    if request.method == 'POST':
        nom_usuario = request.POST['username']
        clave = request.POST['password']
        usuario = authenticate(username = nom_usuario, password = clave)
        if usuario is not None:
            login(request, usuario)
            return HttpResponseRedirect('/crear_itinerario/')
        else:
            return HttpResponseRedirect('/accounts/login/')

def crear_itinerario(request):
    if request.user.is_authenticated():
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
    else:
        return redirect('/accounts/login/')

