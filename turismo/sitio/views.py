from django.shortcuts import render, redirect
from datetime import datetime, date
from django.contrib.auth.models import User
from sitio.models import Itinerario, Dia, Perfil_Usuario, Comentario, Puntaje
from sitio.models import ComentariosDenunciados, ItinerariosDenunciados
from sitio.models import ComentarioDenuncia, ItinerarioDenuncia
from sitio.forms import ItinerarioForm, DiaForm, PerfilForm, ComentarioForm, PuntajeForm
from django.forms import formset_factory
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q
from django.urls import reverse
from datetime import datetime, timedelta
from django.forms.models import inlineformset_factory
from django.forms import modelformset_factory

def inicio(request):
    itinerarios = Itinerario.objects.all().order_by('-fecha').filter(estado = 'Publicado')[:10]
    if request.method == 'POST':
        if "btn_hoy" in request.POST:
            itinerarios = Itinerario.objects.all().order_by('-fecha').filter(fecha__gt = datetime.today() - timedelta(days=1)).filter(estado = 'Publicado')
        if "btn_ultima_semana" in request.POST:
            itinerarios = Itinerario.objects.all().order_by('-fecha').filter(fecha__gt = datetime.today() - timedelta(days=7)).filter(estado = 'Publicado')
        if "btn_mas_visitados" in request.POST:
            itinerarios = Itinerario.objects.all().order_by('-visitas').filter(estado = 'Publicado')[:10]
        if "btn_mejor_puntuacion" in request.POST:
            itinerarios = Itinerario.objects.all().order_by('-valoracion').filter(estado = 'Publicado')[:10]
    return render(request, 'inicio.html', {'lista_itinerarios': itinerarios})

def acerca_de(request):
    return render(request, 'acerca_de.html')

def usuario(request):
    usuarios = User.objects.all()
    return render(request, 'usuario.html', {'lista_usuarios': usuarios})

@login_required
def modificar_itinerario(request, id_itiner):
    itinerario = Itinerario.objects.get(pk=id_itiner)
    q = Dia.objects.filter(itinerario = itinerario)
    DiaFormSet = modelformset_factory(Dia,form = DiaForm, extra = 0, can_delete = True)
    perfil = Perfil_Usuario.objects.filter(usuario = request.user)
    if len(perfil) == 0:
        perfil = None
    else:
        perfil = perfil[0]
    if request.method == 'POST':
        itinerario_form = ItinerarioForm(request.POST, request.FILES, instance = itinerario)
        formset = DiaFormSet(request.POST, request.FILES, queryset= q)
        if itinerario_form.is_valid() and formset.is_valid():
            itinerario = itinerario_form.save(commit=False)
            if 'btn_borrador' in request.POST:
                itinerario.estado = "Borrador"
            else:
                itinerario.estado = "Publicado"
            itinerario.save()
            dias = formset.save()
            for dia in dias:
                dia.itinerario = itinerario
                dia.save()
        if 'btn_agregar' in request.POST:
            nuevo_dia = Dia.objects.crear_dia(itinerario)
            return redirect('/modificar_itinerario/' + str(itinerario.id))
        if 'btn_borrador' in request.POST:
            return redirect('/inicio')
        if 'btn_finalizar' in request.POST:
            return redirect('/ver_itinerario/' + str(itinerario.id))
    else:
        itinerario_form = ItinerarioForm(instance = itinerario)
        formset = DiaFormSet(queryset = q)
    return render(request, 'modificar_itinerario.html', {'form1': itinerario_form, 'form2': formset, 'perfil': perfil})

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

@login_required
def denunciar(request, tipo, id_objeto):
    udenunciante = request.user
    ya_denunciado = 0
    if tipo == "Comentario":
        comentario = Comentario.objects.get(pk = id_objeto)
        cdenuncia = ComentarioDenuncia.objects.filter(usuario_denunciante=udenunciante).filter(comentario=comentario)
        if len(cdenuncia) == 0:
            nueva_denuncia = ComentarioDenuncia.objects.crear_comentariodenuncia(request.user,comentario)
            nueva_denuncia.save()
            cdenunciado = ComentariosDenunciados.objects.filter(usuario_denunciado=comentario.usuario).filter(comentario=comentario)
            if len(cdenunciado) == 0:
                nueva_denuncia = ComentariosDenunciados.objects.crear_comentariodenunciado(comentario.usuario,comentario)
                nueva_denuncia.save()
                cdenunciado = ComentariosDenunciados.objects.filter(usuario_denunciado=comentario.usuario).filter(comentario=comentario)
            clave = cdenunciado[0].id
            cdenunciado = ComentariosDenunciados.objects.get(pk = clave)
            cdenunciado.cantidad += 1
            if cdenunciado.cantidad > 20:
                cdenunciado.usuario.estado = "Restringido"
                comentario.texto = "Este comentario ha sido eliminado por violar los términos y condiciones de Santa Fe por el mundo"
                comentario.save()
            cdenunciado.save()
        else:
            ya_denunciado = 1
    else:
        itinerario = Itinerario.objects.get(pk = id_objeto)
        idenuncia = ItinerarioDenuncia.objects.filter(usuario_denunciante=udenunciante).filter(itinerario=itinerario)
        if len(idenuncia) == 0:
            nueva_denuncia = ItinerarioDenuncia.objects.crear_itinerariodenuncia(request.user,itinerario)
            nueva_denuncia.save()
            idenunciado = ItinerariosDenunciados.objects.filter(usuario_denunciado=itinerario.usuario).filter(itinerario=itinerario)
            if len(idenunciado) == 0:
                nueva_denuncia = ItinerariosDenunciados.objects.crear_itinerariodenunciado(itinerario.usuario,itinerario)
                nueva_denuncia.save()
                idenunciado = ItinerariosDenunciados.objects.filter(usuario_denunciado=itinerario.usuario).filter(itinerario=itinerario)
            clave = idenunciado[0].id
            idenunciado =ItinerariosDenunciados.objects.get(pk = clave)
            idenunciado.cantidad += 1
            if idenunciado.cantidad > 20:
                idenunciado.usuario.estado = "Restringido"
                itinerario.estado = "EliminadoLogicamente"
                itinerario.save()
            idenunciado.save()
        else:
            ya_denunciado = 1
    return render(request, 'denunciar.html', {'ya_denunciado':ya_denunciado})

def ver_itinerario(request,id_itiner):
    itinerario = Itinerario.objects.get(pk = id_itiner)
    itinerario.visitas += 1
    itinerario.save()
    itinerario = Itinerario.objects.get(pk = id_itiner)
    usuario = itinerario.usuario
    dias = Dia.objects.filter(itinerario = itinerario)
    comentarios = Comentario.objects.filter(itinerario = itinerario)
    if not request.user.is_anonymous:
        puntaje = Puntaje.objects.filter(usuario = request.user, itinerario = itinerario)
        if len(puntaje) == 0:
            puntaje = None
        else:
            puntaje = puntaje[0]
    else:
        puntaje = None
    if request.method == 'POST':
        comentario_form = ComentarioForm(request.POST)
        if 'btn_comentar' in request.POST:
            if comentario_form.is_valid():
                comentario = comentario_form.save(commit=False)    
                comentario.fecha = datetime.now()
                comentario.usuario = request.user
                comentario.itinerario = itinerario
                comentario.save()
        else:
            if not request.user.is_anonymous:
                puntaje = Puntaje.objects.filter(usuario = request.user).filter(itinerario = itinerario)
                if len(puntaje) == 0:
                    puntaje_form = PuntajeForm(request.POST)
                    if puntaje_form.is_valid():
                        puntaje = puntaje_form.save(commit=False)
                        puntaje = Puntaje.objects.crear_puntaje(request.user,itinerario, puntaje.calificacion)
                        puntaje.save()
                        puntaje = Puntaje.objects.filter(usuario = request.user).filter(itinerario = itinerario)[0]
                        itinerario.valoracion += puntaje.calificacion
                else:
                    puntaje_form = PuntajeForm(request.POST, instance=puntaje[0])
                    if puntaje_form.is_valid():
                        puntaje = puntaje_form.save(commit=False)
                        aux_puntaje = Puntaje.objects.filter(usuario = request.user).filter(itinerario = itinerario)[0]
                        itinerario.valoracion -= aux_puntaje.calificacion
                        puntaje.save()
                        puntaje = Puntaje.objects.filter(usuario = request.user).filter(itinerario = itinerario)[0]
                        itinerario.valoracion += puntaje.calificacion
        itinerario.save()
        return redirect('/ver_itinerario/' + str(id_itiner))
    else:
        comentario_form = ComentarioForm()
        puntaje_form = PuntajeForm()
    if not request.user.is_anonymous:
        if len(Perfil_Usuario.objects.filter(usuario = request.user)) != 0:
            perfil = Perfil_Usuario.objects.get(usuario = request.user)
            return render(request, 'ver_itinerario.html', {'itinerario': itinerario, 'lista_dias': dias, 'lista_comentarios': comentarios, 'form1': comentario_form, 'form2': puntaje_form, 'perfil': perfil, 'puntaje': puntaje})
        else:
            return render(request, 'ver_itinerario.html', {'itinerario': itinerario, 'lista_dias': dias, 'lista_comentarios': comentarios, 'form1': comentario_form, 'form2': puntaje_form, 'perfil': None, 'puntaje':puntaje})
    else:
        return render(request, 'ver_itinerario.html', {'itinerario': itinerario, 'lista_dias': dias, 'lista_comentarios': comentarios, 'form1': None, 'form2': None, 'perfil': None, 'puntaje': puntaje})

@login_required
def ver_perfil_usuario(request):
    usuario = request.user
    itinerarios = Itinerario.objects.filter(usuario = usuario).order_by('-fecha')[:10]
    if Perfil_Usuario.objects.filter(usuario = usuario).count() == 0:
        idperfil = Perfil_Usuario.objects.count() + 1
        perfil = Perfil_Usuario.objects.crear_perfil(idperfil,usuario)
    else:
        perfil = Perfil_Usuario.objects.filter(usuario = usuario).order_by('-id')[0]
    return render(request, 'perfil.html', {'perfil': perfil, 'usuario': usuario, 'lista_itinerarios': itinerarios})

@login_required
def crear_itinerario(request):
    perfil = Perfil_Usuario.objects.filter(usuario = request.user)
    if len(perfil) == 0:
        perfil = None
    else:
        perfil = perfil[0]
    if request.method == 'POST':
        itinerario_form = ItinerarioForm(request.POST, request.FILES)
        if itinerario_form.is_valid():
            itinerario = itinerario_form.save(commit=False)
            itinerario.fecha = datetime.now()
            itinerario.usuario = request.user
            if 'btn_borrador' in request.POST:
                itinerario.estado = "Borrador"
                itinerario.save()
                return redirect('/inicio/')
            else:
                itinerario.estado = 'PendientePublicacion'
                itinerario.save()
                nuevo_dia = Dia.objects.crear_dia(itinerario)
                return redirect('/modificar_itinerario/' + str(itinerario.id))
    else:
        itinerario_form = ItinerarioForm()
    return render(request, 'crear_itinerario.html', {'form':itinerario_form, 'perfil': perfil})

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