"""turismo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


from sitio.views import inicio, crear_itinerario, ver_perfil_usuario, crear_dia 
from sitio.views import ver_itinerario, acerca_de, modificar_perfil
from sitio.views import modificar_itinerario, eliminar_itinerario, denunciar
urlpatterns = [
    url(r'^$', inicio),
    url(r'^inicio/$', inicio),
    url(r'^acerca_de/$', acerca_de),
    url(r'^admin/', admin.site.urls),
    url(r'^search/', include('haystack.urls')),
    url(r'^crear_itinerario/$', crear_itinerario),
    url(r'^crear_dia/(?P<id_itiner>\d+)/$', crear_dia),
    url(r'^ver_itinerario/(?P<id_itiner>\d+)/$', ver_itinerario),
    url(r'^perfil/$', ver_perfil_usuario),
    url(r'^modificar_perfil/(?P<id_usuario>\d+)/(?P<id_perfil>\d+)/$', modificar_perfil),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^modificar_itinerario/(?P<id_itiner>\d+)/$', modificar_itinerario),
    url(r'^eliminar_itinerario/(?P<id_itiner>\d+)/$', eliminar_itinerario),
    url(r'^denunciar/(?P<id_coment>\d+)/$', denunciar),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
