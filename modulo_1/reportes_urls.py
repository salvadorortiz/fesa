from django.conf.urls import include, url
from django.contrib import admin
from modulo_1 import reportes_views

urlpatterns = [
	url(r'^general/', 'modulo_1.reportes_views.ReportesView',name='reportes'),
	#Reporte de reservas
	url(r'^reservas/', 'modulo_1.reportes_views.ReporteReservaData',name='repo_reserva'),
]