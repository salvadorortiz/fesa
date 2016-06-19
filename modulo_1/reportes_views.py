#-*- coding: utf-8 -*-
from django.shortcuts import render
from funciones_generales import convert_fetchall
from django.db import connection
from django.http import HttpResponse
from modulo_1.forms import ClienteForm, EmpresaForm
from modulo_1.models import Cliente, Empresa,Complejo,Usuario
import json
import hashlib
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def ReportesView(request):
	complejos= Complejo.objects.all()
	print complejos
	cmb_complejo="<option value=''>Seleccione un complejo</option>"
	for complejo in complejos:
		cmb_complejo+="<option value='"+str(complejo.complejo_id)+"'>"+complejo.nombre+"</option>"

	usuarios= Usuario.objects.all()
	cmb_usuario="<option value=''>Seleccione un usuario</option>"
	for user in usuarios:
		cmb_usuario+="<option value='"+str(user.usuario_id)+"'>"+user.nombre+"</option>"
	data={'cmb_complejo':cmb_complejo,
		  'cmb_usuario':cmb_usuario,
	}
	return render(request,'reportes.html',data)

def ReporteReservaData(request):
	filtro=" WHERE 1=1"

	if str(request.POST['fecha_desde'])!= '':
		filtro+=" AND fecha_reserva >= '" + str(request.POST['fecha_desde']) + "'" 

	if str(request.POST['fecha_hasta'])!='':
		filtro+=" AND fecha_reserva <= '" + str(request.POST['fecha_hasta']) + "'"

	if str(request.POST['complejo_id'])!='':
		filtro+=" AND complejo_id = " + str(request.POST['complejo_id'])

	str_query = "SELECT * FROM dt_repo_reserva" + filtro
	#print str_query
	cursor = connection.cursor()
	cursor.execute(str_query)
	qs = cursor.fetchall()
	#print convert_fetchall(qs)
	return HttpResponse(json.dumps(convert_fetchall(qs)), content_type='application/json')

def ReporteClientesData(request):
	str_query = "SELECT * FROM dt_repo_clientes"
	#print str_query
	cursor = connection.cursor()
	cursor.execute(str_query)
	qs = cursor.fetchall()
	#print convert_fetchall(qs)
	return HttpResponse(json.dumps(convert_fetchall(qs)), content_type='application/json')

def ReporteRemesasData(request):
	filtro=" WHERE 1=1"

	if str(request.POST['fecha_desde'])!= '':
		filtro+=" AND fecha_ingreso >= '" + str(request.POST['fecha_desde']) + "'" 

	if str(request.POST['fecha_hasta'])!='':
		filtro+=" AND fecha_ingreso <= '" + str(request.POST['fecha_hasta']) + "'"

	if str(request.POST['usuario_id'])!='':
		filtro+=" AND usuario = " + str(request.POST['usuario_id'])

	str_query = "SELECT * FROM dt_repo_remesa" + filtro
	#print str_query
	cursor = connection.cursor()
	cursor.execute(str_query)
	qs = cursor.fetchall()
	#print convert_fetchall(qs)
	return HttpResponse(json.dumps(convert_fetchall(qs)), content_type='application/json')

def ReporteRemesasTotalData(request):
	filtro=" WHERE 1=1"

	if str(request.POST['fecha_desde'])!= '':
		filtro+=" AND where to_char(res.fecha_ingreso, 'YYYY-MM-DD') >= '" + str(request.POST['fecha_desde']) + "'" 

	if str(request.POST['fecha_hasta'])!='':
		filtro+=" AND where to_char(res.fecha_ingreso, 'YYYY-MM-DD') <= '" + str(request.POST['fecha_hasta']) + "'"

	if str(request.POST['usuario_id'])!='':
		filtro+=" AND res.usuario_id = " + str(request.POST['usuario_id'])

	str_query = "SELECT \
		'$'|| COALESCE(to_char(SUM(res.precio),'9G999.99'),to_char(0,'9G999.99')) as precio_total,\
		'$'|| COALESCE(to_char(SUM(res.costo),'9G999.99'),to_char(0,'9G999.99')) as costo_total,\
		'$'|| COALESCE(to_char(SUM(res.precio) - SUM(res.costo),'9G999.99'),to_char(0,'9G999.99')) as utilidad_total,\
		'$'|| COALESCE(to_char(SUM(rr.monto),'9G999.99'),to_char(0,'9G999.99')) as remanente_total\
		FROM modulo_1_remesaxreserva rr \
		inner join modulo_1_reserva res on res.reserva_id=rr.reserva_id" +filtro
	#print str_query
	cursor = connection.cursor()
	cursor.execute(str_query)
	qs = cursor.fetchall()
	#print convert_fetchall(qs)
	return HttpResponse(json.dumps(convert_fetchall(qs)), content_type='application/json')