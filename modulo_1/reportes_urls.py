from django.conf.urls import include, url
from django.contrib import admin
from modulo_1 import reportes_views

urlpatterns = [
	url(r'^general/', 'modulo_1.reportes_views.ReportesView',name='reportes'),
	#Reporte de reservas
	url(r'^reservas/', 'modulo_1.reportes_views.ReporteReservaData',name='repo_reserva'),
	url(r'^clientes/', 'modulo_1.reportes_views.ReporteClientesData',name='repo_clientes'),
	url(r'^remesas/', 'modulo_1.reportes_views.ReporteRemesasData',name='repo_remesas'),
	url(r'^total/', 'modulo_1.reportes_views.ReporteRemesasTotalData',name='repo_total'),
	url(r'^cliente_eventos/', 'modulo_1.reportes_views.EventosClientesData',name='repo_evento_cliente'),
	url(r'^horas_cancha/', 'modulo_1.reportes_views.ReporteHorasCanchaData',name='repo_horas_cancha'),

]