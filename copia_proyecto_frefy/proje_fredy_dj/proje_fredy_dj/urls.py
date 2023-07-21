"""proje_fredy_dj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from proje_fredy_dj.views import hola_mundo
from core import views as core_views #aplicacion core
from portafolio import views as portafolio_views #alias
from registration import views as registration_views
from empresa import views as empresa_views
from contacto import views as contacto_views#alias
from django.urls import path,include #agregue nuevo
from django.conf import settings #


urlpatterns = [
    path('',core_views.home, name='inicio'),
    
    path('accounts/', include('django.contrib.auth.urls')),#IMPORTAR LA LIBRERIA PARA PODER UTILIZARLA EN EL LOGIN
    path('accounts/', include('registration.urls')),
    
    #path('registro', registration_views.registro, name='registro'),
    path('contacto/', include('contacto.urls')),#hice este cambio
    path('portafolio/',portafolio_views.portafolio, name='portafolio'),
    path('empresa/', empresa_views.variable, name='empresa'),
    path('productos/',portafolio_views.productos, name='productos'),
    path('about/',core_views.about, name='acerca'),
    path('admin/', admin.site.urls),#administracion
]
if settings.DEBUG: #configurar
    from django.conf.urls.static import static
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT
                        )