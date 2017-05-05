from django.shortcuts import render, redirect
from datetime import datetime, date
from django.contrib.auth.models import User
from sitio.models import Itinerario, Estado, Dia, Pais, Perfil_Usuario
from sitio.forms import ItinerarioForm, DiaForm, PerfilForm
from django.forms import formset_factory
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q
from django.urls import reverse


def inicio(request):
    itinerarios = Itinerario.objects.all()
    return render(request, 'inicio.html', {'lista_itinerarios': itinerarios})

def acerca_de(request):
    return render(request, 'acerca_de.html')

def usuario(request):
    usuarios = User.objects.all()
    return render(request, 'usuario.html', {'lista_usuarios': usuarios})

def modificar_perfil(request, id_perfil):
    if request.method == 'POST':
        perfil_form = PerfilForm(request.POST, request.FILES)
        if perfil_form.is_valid():
            perfil = perfil_form.save(commit=False)
            perfil.usuario = request.user
            perfil.save()
            return redirect('/perfil/')
    else:
        perfil_form = PerfilForm()

    return render(request, 'modificar_perfil.html', {'form': perfil_form})

def ver_itinerario(request,id_itiner):
    itinerario = Itinerario.objects.get(pk = id_itiner)
    dias = Dia.objects.filter(itinerario = itinerario)
    return render(request, 'ver_itinerario.html', {'itinerario': itinerario, 'lista_dias': dias})

'''def ver_perfil_usuario(request):
    usu = request.user
    perfil = Perfil_Usuario.objects.filter(usuario = usu).order_by('-id')[:1]
    id_perfil = perfil[0].id
    if request.method == 'POST':
        return redirect('/modificar_perfil/' + str(id_perfil))
    return render(request, 'perfil.html', {'perfil': perfil, 'id_perfil': id_perfil})'''

@login_required
def crear_itinerario(request):
    #dias = (itinerario.fecha_salida - itinerario.fecha_llegada).days
    #DiasFormSet = formset_factory(form=DiaForm, extra=10)
    #formset = DiasFormSet(request.POST)
    if request.method == 'POST':
        itinerario_form = ItinerarioForm(request.POST, request.FILES)
        if itinerario_form.is_valid():
            itinerario = itinerario_form.save(commit=False)
            itinerario.fecha = datetime.now()
            itinerario.usuario = request.user
            if 'btn_borrador' in request.POST:
                estado = Estado.objects.get(pk = 3)
                itinerario.estado = estado
                itinerario.save()
                return redirect('/inicio/')
            else:
                estado = Estado.objects.get(pk = 1)
                itinerario.estado = estado
                itinerario.save()
                return redirect('/crear_dia/' + str(itinerario.id))
    else:
        itinerario_form = ItinerarioForm()

    return render(request, 'crear_itinerario.html', {'form':itinerario_form})#,'formset':formset})

@login_required
def crear_dia(request, id_itiner):
    if request.method == 'POST':
        dia_form = DiaForm(request.POST, request.FILES)
        if dia_form.is_valid():
            dia = dia_form.save(commit=False)
            itinerario = Itinerario.objects.get(pk = id_itiner)
            dia.itinerario = itinerario
            dia.save()
            if 'btn_guardar_agregar' in request.POST:
                redirect('/crear_dia/' + str(id_itiner))
            else:
                estado = Estado.objects.get(pk = 2)
                itinerario.estado = estado
                itinerario.save()
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


