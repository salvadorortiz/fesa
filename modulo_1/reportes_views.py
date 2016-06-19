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

def EventosClientesData(request):
	str_query = "SELECT * from dt_repo_cliente_eventos where tipo_registro="+str(request.POST['tipo_registro'])
	str_query+= " AND id_registro="+str(request.POST['id_registro']) 
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
		filtro+=" AND to_char(res.fecha_ingreso, 'YYYY-MM-DD') >= '" + str(request.POST['fecha_desde']) + "'" 

	if str(request.POST['fecha_hasta'])!='':
		filtro+=" AND to_char(res.fecha_ingreso, 'YYYY-MM-DD') <= '" + str(request.POST['fecha_hasta']) + "'"

	if str(request.POST['usuario_id'])!='':
		filtro+=" AND res.usuario_id = " + str(request.POST['usuario_id'])

	str_query = "SELECT\
				 COALESCE(res.precio,0) as precio_total,\
				COALESCE(res.costo,0) as costo_total,\
				COALESCE(res.precio - res.costo,0) as utilidad_total,\
				COALESCE(SUM(rr.monto),0) as remanente_total\
				FROM modulo_1_remesaxreserva rr \
				right join modulo_1_reserva res on rr.reserva_id=res.reserva_id\
				" +filtro +" group by res.reserva_id"
	#print str_query
	cursor = connection.cursor()
	cursor.execute(str_query)
	qs = cursor.fetchall()
	print convert_fetchall_total(qs)
	return HttpResponse(json.dumps(convert_fetchall_total(qs)), content_type='application/json')

def convert_fetchall_total(cursor):
	dict_cursor={}
	list_aux=[]
	list_totales=[0,0,0,0]
	for item in cursor:
		#print "\n item -->",item
		list_totales[0]+=float(item[0])
		list_totales[1]+=float(item[1])
		list_totales[2]+=float(item[2])
		list_totales[3]+=float(item[3])
	#print "totall--->",list_totales

	list_aux.append(['$'+str(list_totales[0]),'$'+str(list_totales[1]),'$'+str(list_totales[2]),'$'+str(list_totales[3])])
	dict_cursor['recordsTotal']=len(list_aux)
	dict_cursor['recordsFiltered']=len(list_aux)
	dict_cursor['draw']= len(list_aux)//10
	dict_cursor['data']=list_aux
	return dict_cursor