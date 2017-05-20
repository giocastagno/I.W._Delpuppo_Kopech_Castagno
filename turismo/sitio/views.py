from django.shortcuts import render, redirect
from datetime import datetime, date
from django.contrib.auth.models import User
from sitio.models import Itinerario, Dia, Perfil_Usuario, Comentario
from sitio.forms import ItinerarioForm, DiaForm, PerfilForm, ComentarioForm
from django.forms import formset_factory
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q
from django.urls import reverse


def inicio(request):
    itinerarios = Itinerario.objects.all().order_by('-fecha').filter(estado = 'Publicado')[:10]
    return render(request, 'inicio.html', {'lista_itinerarios': itinerarios})

def acerca_de(request):
    return render(request, 'acerca_de.html')

def usuario(request):
    usuarios = User.objects.all()
    return render(request, 'usuario.html', {'lista_usuarios': usuarios})

@login_required
def modificar_itinerario(request, id_itiner):
    itinerario = Itinerario.objects.get(pk=id_itiner)
    if request.method == 'POST':
        itinerario_form = ItinerarioForm(request.POST, request.FILES, instance = itinerario)
        if itinerario_form.is_valid():
            itinerario = itinerario_form.save(commit=False)
            itinerario.estado = "Publicado"
            itinerario.save()
            return redirect('/ver_itinerario/' + str(itinerario.id))
    else:
        itinerario_form = ItinerarioForm(instance = itinerario)
    return render(request, 'modificar_itinerario.html', {'form': itinerario_form})   

@login_required
def eliminar_itinerario(request, id_itiner):
    itinerario = Itinerario.objects.get(pk=id_itiner)
    itinerario.estado = 'EliminadoLogicamente'
    itinerario.save()
    return render(request, 'eliminar_itinerario.html')

@login_required
def modificar_perfil(request, id_usuario, id_perfil):
    perfil = Perfil_Usuario.objects.get(pk=id_perfil)
    usuario = User.objects.get(pk = id_usuario)
    if request.method == 'POST':
        perfil_form = PerfilForm(request.POST, request.FILES, instance = perfil)
        if perfil_form.is_valid():
            perfil = perfil_form.save(commit=False)
            perfil.usuario = request.user
            perfil.save()
            return redirect('/perfil/')
    else:
        perfil_form = PerfilForm(instance = perfil)

    return render(request, 'modificar_perfil.html', {'form': perfil_form})

def ver_itinerario(request,id_itiner):
    itinerario = Itinerario.objects.get(pk = id_itiner)
    itinerario.visitas += 1
    itinerario.save()
    itinerario = Itinerario.objects.get(pk = id_itiner)
    usuario = itinerario.usuario
    dias = Dia.objects.filter(itinerario = itinerario)
    comentarios = Comentario.objects.filter(itinerario = itinerario)
    if request.method == 'POST':
        comentario_form = ComentarioForm(request.POST)
        if comentario_form.is_valid():
            comentario = comentario_form.save(commit=False)
            comentario.fecha = datetime.now()
            comentario.usuario = request.user
            comentario.itinerario = itinerario
            comentario.save()
            #comentarios = Comentario.objects.filter(itinerario = itinerario)
            #comentario = comentarios[len(comentarios)-1]
            if comentario.calificacion == 'Excelente':
                itinerario.valoracion += 5
            if comentario.calificacion == 'Muy Bueno':
                itinerario.valoracion += 4
            if comentario.calificacion == 'Bueno':
                itinerario.valoracion += 3
            if comentario.calificacion == 'Regular':
                itinerario.valoracion += 2
            if comentario.calificacion == 'Malo':
                itinerario.valoracion += 1
            itinerario.save()
            return redirect('/ver_itinerario/' + str(id_itiner))
    else:
        comentario_form = ComentarioForm()
    return render(request, 'ver_itinerario.html', {'itinerario': itinerario, 'lista_dias': dias, 'lista_comentarios': comentarios, 'form': comentario_form})

def ver_perfil_usuario(request):
    usuario = request.user
    itinerarios = Itinerario.objects.filter(usuario = usuario).order_by('-fecha')

    
    if Perfil_Usuario.objects.filter(usuario = usuario).count() == 0:
        idperfil = Perfil_Usuario.objects.count() + 1
        perfil = Perfil_Usuario.objects.crear_perfil(idperfil,usuario)
    else:
        perfil = Perfil_Usuario.objects.filter(usuario = usuario).order_by('-id')[0]
    return render(request, 'perfil.html', {'perfil': perfil, 'usuario': usuario, 'lista_itinerarios': itinerarios})

@login_required
def crear_itinerario(request):
    if request.method == 'POST':
        itinerario_form = ItinerarioForm(request.POST, request.FILES)
        if itinerario_form.is_valid():
            itinerario = itinerario_form.save(commit=False)
            itinerario.fecha = datetime.now()
            itinerario.usuario = request.user
            if 'btn_borrador' in request.POST:
                itinerario.estado = 'Borrador'
                itinerario.save()
                return redirect('/inicio/')
            else:
                itinerario.estado = 'PendientePublicacion'
                itinerario.save()
                return redirect('/crear_dia/' + str(itinerario.id))
    else:
        itinerario_form = ItinerarioForm()

    return render(request, 'crear_itinerario.html', {'form':itinerario_form})

@login_required
def crear_dia(request, id_itiner):
    itinerario = Itinerario.objects.get(pk = id_itiner)
    dias = Dia.objects.filter(itinerario = itinerario)
    if request.method == 'POST':
        dia_form = DiaForm(request.POST, request.FILES)
        if dia_form.is_valid():
            dia = dia_form.save(commit=False)
            dia.itinerario = itinerario
            dia.fecha = datetime.now()
            dia.usuario = request.user
            dia.save()
            if 'btn_guardar_agregar' in request.POST:
                return HttpResponseRedirect(request.path)
            else:
                itinerario.estado = 'Publicado'
                itinerario.save()
                return redirect('/inicio/')
    else:
        dia_form = DiaForm()

    return render(request, 'crear_dia.html', {'form': dia_form, 'lista_dias':dias})

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


