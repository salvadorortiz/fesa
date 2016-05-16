from django.conf.urls import include, url
from django.contrib import admin
from modulo_1 import cliente_views

urlpatterns = [
    url(r'^cliente/', 'modulo_1.cliente_views.RegistroClienteView',name='cliente_registrocliente'),
    url(r'^precios/', 'modulo_1.views.PreciosView',name='precios_guia'),
]