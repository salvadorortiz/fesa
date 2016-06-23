#-*- coding: utf-8 -*-
from django.shortcuts import render
from funciones_generales import convert_fetchall
from django.db import connection
from django.http import HttpResponse
from modulo_1.forms import ClienteForm, EmpresaForm
from modulo_1.models import Cliente, Empresa,Complejo,Usuario,TipoAlquiler
import json
import hashlib
import sys
from datetime import date,datetime

reload(sys)
sys.setdefaultencoding('utf-8')

def ReportesView(request):
	#ReporteHorasCancha()
	complejos= Complejo.objects.all()
	#print  complejos
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
	##print  str_query
	cursor = connection.cursor()
	cursor.execute(str_query)
	qs = cursor.fetchall()
	##print  convert_fetchall(qs)
	return HttpResponse(json.dumps(convert_fetchall(qs)), content_type='application/json')

def ReporteClientesData(request):
	str_query = "SELECT * FROM dt_repo_clientes"
	##print  str_query
	cursor = connection.cursor()
	cursor.execute(str_query)
	qs = cursor.fetchall()
	##print  convert_fetchall(qs)
	return HttpResponse(json.dumps(convert_fetchall(qs)), content_type='application/json')

def EventosClientesData(request):
	str_query = "SELECT * from dt_repo_cliente_eventos where tipo_registro="+str(request.POST['tipo_registro'])
	str_query+= " AND id_registro="+str(request.POST['id_registro']) 
	##print  str_query
	cursor = connection.cursor()
	cursor.execute(str_query)
	qs = cursor.fetchall()
	##print  convert_fetchall(qs)
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
	##print  str_query
	cursor = connection.cursor()
	cursor.execute(str_query)
	qs = cursor.fetchall()
	##print  convert_fetchall(qs)
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
				COALESCE(res.precio,0)-COALESCE(SUM(rr.monto),0) as remanente_total\
				FROM modulo_1_remesaxreserva rr \
				right join modulo_1_reserva res on rr.reserva_id=res.reserva_id\
				" +filtro +" group by res.reserva_id"
	##print  str_query
	cursor = connection.cursor()
	cursor.execute(str_query)
	qs = cursor.fetchall()
	#print  convert_fetchall_total(qs)
	return HttpResponse(json.dumps(convert_fetchall_total(qs)), content_type='application/json')

def convert_fetchall_total(cursor):
	dict_cursor={}
	list_aux=[]
	list_totales=[0,0,0,0]
	for item in cursor:
		##print  "\n item -->",item
		list_totales[0]+=float(item[0])
		list_totales[1]+=float(item[1])
		list_totales[2]+=float(item[2])
		list_totales[3]+=float(item[3])
	##print  "totall--->",list_totales

	list_aux.append(['$'+str(list_totales[0]),'$'+str(list_totales[1]),'$'+str(list_totales[2]),'$'+str(list_totales[3])])
	dict_cursor['recordsTotal']=len(list_aux)
	dict_cursor['recordsFiltered']=len(list_aux)
	dict_cursor['draw']= len(list_aux)//10
	dict_cursor['data']=list_aux
	return dict_cursor

def ReporteHorasCancha(request):
	total_horas_posibles=0
	total_horas_usadas=0
	##print  "\n \n -----------------------------------"
	filtro=" WHERE 1=1"

	if str(request.POST['fecha_desde'])!= '':
		filtro+=" AND fecha_ingreso >= '" + str(request.POST['fecha_desde']) + "'" 

	if str(request.POST['fecha_hasta'])!='':
		filtro+=" AND fecha_ingreso <= '" + str(request.POST['fecha_hasta']) + "'"

	if str(request.POST['complejo_id'])!='':
		filtro+=" AND complejo_id = " + str(request.POST['complejo_id'])
		if str(request.POST['fecha_desde'])== '' and str(request.POST['fecha_hasta'])=='':
			filtro+=" UNION SELECT * FROM dt_repo_horas Where complejo_id="+ str(request.POST['complejo_id'])
			filtro+=" AND fecha_ingreso is null"

	str_query = "SELECT * FROM dt_repo_horas" + filtro
	cursor = connection.cursor()
	cursor.execute(str_query)
	qs = cursor.fetchall()
	##print  qs
	qs_alquiler= TipoAlquiler.objects.all().order_by('nombre')
	##print  qs_alquiler
	tuples_resultado=[]
	for item in qs:
		#print  "\n -->",item
		#verifica que no exista alguna tupla con sus datos 
		if verificar_existencia(item,tuples_resultado):
			for tipo_a in qs_alquiler:
				tupla_aux= [int(item[0]),int(item[1]),int(tipo_a.tipo_alquiler_id),str(item[4]),str(tipo_a.nombre),0]
				##print  "AUX->",tupla_aux
				tuples_resultado.append(tupla_aux)

			#if item[6] is not None:
			#	total_horas_posibles+=(time_to_int(item[6])/7)
			#else:
			#	total_horas_posibles+=(float(item[7])/7)
		
			#print  "HPPP-->",total_horas_posibles

	for item in qs:
		##print  "\n -->",item
		for tupla in tuples_resultado:
			##print  tupla
			if item[2] is not None:
				if int(item[0])==int(tupla[0]) and int(item[1])==int(tupla[1]) and int(item[2])==int(tupla[2]):
					##print  "\n -->",time_to_int(item[5])
					tupla[5]+=time_to_int(item[5])
					total_horas_usadas+=time_to_int(item[5])

	lista_resultado=[]				
#-------------------------------------------------------------------------------------------
	filtro_horas=" WHERE 1=1"
	if str(request.POST['complejo_id'])!='':
		filtro_horas+=" AND complejo_id = " + str(request.POST['complejo_id'])

	str_query = "SELECT * FROM dt_repo_horasposibles" + filtro_horas
	cursor = connection.cursor()
	cursor.execute(str_query)
	repo_horas = cursor.fetchall()
	for hora in repo_horas:
		print "\n",hora
		total_horas_posibles+=time_to_int(hora[2])/7
#--------------------------------------------------------------------------------------------
	for item in tuples_resultado:
		item.append(total_horas_posibles)
		item.append(total_horas_usadas)
		##print  "\n",item
		lista_resultado.append(tuple(item))
	return lista_resultado

	##print  "\n TOTAL HORAS POSIBLES --> ", total_horas_posibles
	##print  "\n TOTAL HORAS USADAS -->",total_horas_usadas

def ReporteHorasCanchaData(request):
	fetch=convert_fetchall(ReporteHorasCancha(request))

	return HttpResponse(json.dumps(fetch), content_type='application/json')

def time_to_int(tiempo):
	arr_tiempo= tiempo.split(':')
	cont=0
	cont+=float(arr_tiempo[0])
	if int(arr_tiempo[1]) == 30:
		cont+=0.5
	return cont

#Retorna true si no existe en la tupla
def verificar_existencia(item,tuplas):
	for tupla in tuplas:
		if int(item[0]) == int(tupla[0]) and int(item[1]) == int(tupla[1]):
			return False
	return True

def calcular_horas_posibles(request):
	try:
		arr_hasta= request.POST['fecha_hasta'].split('-')
		#print  arr_hasta
		arr_desde= request.POST['fecha_desde'].split('-')
		#d0 = date(int(arr_desde[0]), int(arr_desde[1]), int(arr_desde[2]))
		##print  d0
		#d1 = date(int(arr_hasta[0]), int(arr_hasta[1]), int(arr_desde[2]))
		d0=datetime.strptime(str(request.POST['fecha_desde']), "%Y-%m-%d").date()
		d1=datetime.strptime(str(request.POST['fecha_hasta']), "%Y-%m-%d").date()
		delta = d0 - d1
		cantidad_dias= delta.days-1
		print  "Cantidad de dias-->",cantidad_dias
		if cantidad_dias < 0: #esta bien :3
			resultado= float(request.POST['horas_posibles'])*(-1*cantidad_dias)
			##print  resultado
			fetch={'resultado':resultado}
		elif cantidad_dias==0:	#tambien esta bien
			resultado= float(request.POST['horas_posibles'])
			fetch={'resultado':resultado}
		else: #no esta bien :c
			fetch={'errors':1}
	except:
		fetch={'errors':1}
	return HttpResponse(json.dumps(fetch), content_type='application/json')