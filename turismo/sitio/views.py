from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.models import User
from sitio.models import Itinerario, Estado, Dia, Pais
from sitio.forms import ItinerarioForm, DiaForm
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
        itinerario_form = ItinerarioForm(request.POST, request.FILES)
        if itinerario_form.is_valid():
            itinerario = itinerario_form.save(commit=False)
            itinerario.fecha = datetime.now()
            if 'borrador' in request.POST:
                itinerario.estado = 'borrador'
                itinerario.save()
                return redirect('/inicio/')
            else:
                itinerario.save()
                id_itinerario = itinerario.id
                return redirect('/crear_dia/'+str(itinerario.id), pk=str(itinerario.id))
    else:
        itinerario_form = ItinerarioForm()

    return render(request, 'crear_itinerario.html', {'form': itinerario_form},)

@login_required
def crear_dia(request):
    if request.method == 'POST':
        id_itinerario = request.POST.get(pk)
        dia_form = DiaForm(request.POST)
        if dia_form.is_valid():
            dia = dia_form.save(commit=False)
            dia.itinerario = id_itinerario
            dia.fecha = datetime.now()
            dia.save()
            return redirect('/inicio/')
    else:
        dia_form = DiaForm()

    return render(request, 'crear_dia.html', {'form': dia_form})

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


