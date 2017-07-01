# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib.auth.views import logout
from django.contrib import admin
from sopa.views import *
from sopa import views
from django.conf.urls import handler404, handler500



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login$', Login.as_view(), name="login"),
    url(r'^$', views.home,name='home'),
    url(r'^logout$', logout, name="logout", kwargs={'next_page': '/'}),
    url(r'^new_user$', RegistroUsuario.as_view(), name='nuevo_usuario'),
    url(r'^empresas/$', views.lista_empresas, name='lista_empresas'),
    url(r'^empresas/new/$', crearempresa.as_view(), name='nueva_Empresa'),
    url(r'^empresas/(?P<pk>.+)/$', views.detalle_empresa, name='detalle_empresa'),
    url(r'^usuarios/miperfil/$', views.miperfil, name='mi_perfil'),
    url(r'^usuarios/$', views.lista_usuarios, name='lista_usuarios'),
    url(r'^usuarios/(?P<u>.+)/$', views.detalle_usuario, name='detalle_usuarios'),
    url(r'^encuesta/$', views.lista_encuestas, name='lista_encuestas'),
    url(r'^encuesta/nueva/(?P<e>.+)/(?P<d>.+)/(?P<t>.+)$', EncuestaWizard.as_view([PreguntasFundamentalesForm, PreguntasBasicasForm, PreguntasOpcionalesForm, PreguntasAnecdoticasForm])),
    url(r'^encuesta/detalle/(?P<pk>.+)/$', views.detalle_encuesta, name='detalle_encuesta'),
    url(r'^encuesta/eliminar/(?P<pk>.+)/$', views.eliminar_encuesta, name='eliminar_encuesta'),
    url(r'^ayuda/$', views.ayuda, name='ayuda'),
    ]

handler400 = 'sopa.views.handler404'
handler500 = 'sopa.views.handler500'
