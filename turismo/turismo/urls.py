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


from sitio.views import inicio, crear_itinerario, usuario, crear_dia, ver_itinerario, acerca_de
urlpatterns = [
    url(r'^$', inicio),
    url(r'^inicio/$', inicio),
    url(r'^acerca_de/$', acerca_de),
    url(r'^admin/', admin.site.urls),
    url(r'^crear_itinerario/$', crear_itinerario),
    url(r'^crear_dia/(?P<id_itiner>\d+)/$', crear_dia),
    url(r'^ver_itinerario/(?P<id_itiner>\d+)/$', ver_itinerario),
    url(r'^usuario/$', usuario),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
