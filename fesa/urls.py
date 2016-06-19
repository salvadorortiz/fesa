"""fesa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from modulo_1 import registro_urls as registro_urls
from modulo_1 import reportes_urls as reportes_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','fesa.views.login', name='login'),
    url(r'^home','fesa.views.home', name='home'),
    url(r'^password','fesa.views.change_pass', name='change_pass'),
    url(r'^registro/', include(registro_urls)),
    url(r'^reportes/', include(reportes_urls)),
]
