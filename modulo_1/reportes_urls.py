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
	url(r'^calcular_horas_posibles/', 'modulo_1.reportes_views.calcular_horas_posibles',name='calcular_horas_posibles'),
	url(r'^top_clientes/', 'modulo_1.reportes_views.TopClientesData',name='top_clientes'),
	url(r'^top_empresa/', 'modulo_1.reportes_views.TopEmpresaData',name='top_empresa'),
	url(r'^obtener_div_horas/', 'modulo_1.reportes_views.obtener_div_horas',name='obtener_div_horas'),
	
]