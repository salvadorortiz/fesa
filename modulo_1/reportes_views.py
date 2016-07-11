#-*- coding: utf-8 -*-
from django.shortcuts import render
from funciones_generales import convert_fetchall
from django.db import connection
from django.http import HttpResponse
from modulo_1.forms import ClienteForm, EmpresaForm
from modulo_1.models import Cliente, Empresa,Complejo,Usuario,TipoAlquiler,Cancha
import json
import hashlib
import sys
import math
from datetime import date,datetime

reload(sys)
sys.setdefaultencoding('utf-8')

def ReportesView(request):
	#ReporteHorasCancha()
	complejos= Complejo.objects.all()
	###print   complejos
	cmb_complejo="<option value=''>Seleccione un complejo</option>"
	for complejo in complejos:
		cmb_complejo+="<option value='"+str(complejo.complejo_id)+"'>"+complejo.nombre+"</option>"

	canchas= Cancha.objects.all()
	###print   complejos
	cmb_cancha="<option value=''>Seleccione una cancha</option>"
	for cancha in canchas:
		cmb_cancha+="<option value='"+str(cancha.cancha_id)+"'>"+cancha.nombre+"</option>"


	usuarios= Usuario.objects.all()
	cmb_usuario="<option value=''>Seleccione un usuario</option>"
	for user in usuarios:
		cmb_usuario+="<option value='"+str(user.usuario_id)+"'>"+user.nombre+"</option>"

	###print  "\n\n\nRESULTADO HTML --->", html

	data={'cmb_complejo':cmb_complejo,
		  'cmb_usuario':cmb_usuario,
		  'cmb_cancha':cmb_cancha,
		  #'html_horas': html,
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
	##print   str_query
	cursor = connection.cursor()
	cursor.execute(str_query)
	qs = cursor.fetchall()
	####print   convert_fetchall(qs)
	return HttpResponse(json.dumps(convert_fetchall(qs)), content_type='application/json')

def ReporteClientesData(request):
	str_query = "SELECT * FROM dt_repo_clientes"
	####print   str_query
	cursor = connection.cursor()
	cursor.execute(str_query)
	qs = cursor.fetchall()
	####print   convert_fetchall(qs)
	return HttpResponse(json.dumps(convert_fetchall(qs)), content_type='application/json')

def EventosClientesData(request):
	str_query = "SELECT * from dt_repo_cliente_eventos where tipo_registro="+str(request.POST['tipo_registro'])
	str_query+= " AND id_registro="+str(request.POST['id_registro']) 
	####print   str_query
	cursor = connection.cursor()
	cursor.execute(str_query)
	qs = cursor.fetchall()
	####print   convert_fetchall(qs)
	return HttpResponse(json.dumps(convert_fetchall(qs)), content_type='application/json')

def ReporteRemesasData(request):
	filtro=" WHERE 1=1"

	if str(request.POST['fecha_desde'])!= '':
		filtro+=" AND fecha_ingreso >= '" + str(request.POST['fecha_desde']) + "'" 

	if str(request.POST['fecha_hasta'])!='':
		filtro+=" AND fecha_ingreso <= '" + str(request.POST['fecha_hasta']) + "'"

	if str(request.POST['usuario_id'])!='':
		filtro+=" AND usuario = " + str(request.POST['usuario_id'])

	if str(request.POST['deudores'])=='true':
		filtro+=" AND remanente > 0 "

	if 'complejo_id' in request.POST.keys() and str(request.POST['complejo_id'])!='':
		str_query="SELECT repo.reserva_id,repo.fecha_ingreso,repo.nombre_evento,\
		repo.nombre_cliente,repo.nombre_usuario,repo.precio,repo.costo,repo.utilidad,repo.remesado,\
		repo.remanente_2,repo.usuario,repo.remanente\
		 FROM dt_repo_remesa repo\
		LEFT JOIN modulo_1_reservacancha recan ON recan.reserva_id=repo.reserva_id\
		LEFT JOIN modulo_1_cancha can ON can.cancha_id=recan.cancha_id\
		WHERE can.complejo_id= "+str(request.POST['complejo_id'])+" GROUP BY repo.reserva_id,repo.fecha_ingreso,repo.nombre_evento,\
		repo.nombre_cliente,repo.precio,repo.costo,repo.utilidad,repo.remesado,repo.nombre_usuario,\
		repo.remanente_2,repo.usuario,repo.remanente,can.complejo_id"

	else:
		str_query = "SELECT * FROM dt_repo_remesa" + filtro

	#print 'remesa---> ',str_query
	cursor = connection.cursor()
	cursor.execute(str_query)
	qs = cursor.fetchall()
	return HttpResponse(json.dumps(convert_fetchall(qs)), content_type='application/json')

def ReporteRemesasTotalData(request):
	filtro=" WHERE 1=1"

	if str(request.POST['fecha_desde'])!= '':
		filtro+=" AND fecha_ingreso >= '" + str(request.POST['fecha_desde']) + "'" 

	if str(request.POST['fecha_hasta'])!='':
		filtro+=" AND fecha_ingreso <= '" + str(request.POST['fecha_hasta']) + "'"

	if str(request.POST['usuario_id'])!='':
		filtro+=" AND usuario = " + str(request.POST['usuario_id'])

	if str(request.POST['deudores'])=='true':
		filtro+=" AND remanente > 0 "

	if 'complejo_id' in request.POST.keys() and str(request.POST['complejo_id'])!='':
		str_query="SELECT repo.reserva_id,repo.fecha_ingreso,repo.nombre_evento,\
		repo.nombre_cliente,repo.nombre_usuario,repo.precio,repo.costo,repo.utilidad,repo.remesado,\
		repo.remanente_2,repo.usuario,repo.remanente\
		 FROM dt_repo_remesa repo\
		LEFT JOIN modulo_1_reservacancha recan ON recan.reserva_id=repo.reserva_id\
		LEFT JOIN modulo_1_cancha can ON can.cancha_id=recan.cancha_id\
		WHERE can.complejo_id= "+str(request.POST['complejo_id'])+" GROUP BY repo.reserva_id,repo.fecha_ingreso,repo.nombre_evento,\
		repo.nombre_cliente,repo.precio,repo.costo,repo.utilidad,repo.remesado,repo.nombre_usuario,\
		repo.remanente_2,repo.usuario,repo.remanente,can.complejo_id"

	else:
		str_query = "SELECT * FROM dt_repo_remesa" + filtro

	#print   "remesa total--->  ",str_query
	cursor = connection.cursor()
	cursor.execute(str_query)
	qs = cursor.fetchall()
	###print   convert_fetchall_total(qs)
	return HttpResponse(json.dumps(convert_fetchall_total(qs)), content_type='application/json')

def convert_fetchall_total(cursor):
	#print cursor
	dict_cursor={}
	list_aux=[]
	list_totales=[0,0,0,0,0]
	for item in cursor:
		list_totales[0]+=float(money_to_float(item[5]))
		list_totales[1]+=float(money_to_float(item[6]))
		list_totales[2]+=float(money_to_float(item[7]))
		list_totales[3]+=float(money_to_float(item[8]))
		list_totales[4]+=float(money_to_float(item[9]))
	####print   "totall--->",list_totales

	list_aux.append(['$'+str(list_totales[0]),'$'+str(list_totales[1]),'$'+str(list_totales[2]),'$'+str(list_totales[3]),'$'+str(list_totales[4])])
	dict_cursor['recordsTotal']=len(list_aux)
	dict_cursor['recordsFiltered']=len(list_aux)
	dict_cursor['draw']= len(list_aux)//10
	dict_cursor['data']=list_aux
	return dict_cursor

def money_to_float(money):
	arr_money=money.split('$')
	return float(arr_money[1])

def ReporteHorasCancha(request):
	total_horas_posibles=0
	total_horas_usadas=0
	####print   "\n \n -----------------------------------"
	filtro=" WHERE 1=1"

	if 'cancha_id' in request.POST.keys() and str(request.POST['cancha_id'])!='':
		filtro+=" AND cancha_id = " + str(request.POST['cancha_id'])
		# filtro+=" UNION SELECT * FROM dt_repo_horas Where cancha_id="+ str(request.POST['cancha_id'])
		# filtro+=" AND fecha_ingreso is null"

	if 'fecha_desde' in request.POST.keys() and str(request.POST['fecha_desde'])!= '':
		filtro+=" AND fecha_ingreso >= '" + str(request.POST['fecha_desde']) + "'" 

	if 'fecha_hasta' in request.POST.keys() and str(request.POST['fecha_hasta'])!='':
		filtro+=" AND fecha_ingreso <= '" + str(request.POST['fecha_hasta']) + "'"

	if 'complejo_id' in request.POST.keys() and str(request.POST['complejo_id'])!='':
		filtro+=" AND complejo_id = " + str(request.POST['complejo_id'])
		#if str(request.POST['fecha_desde'])== '' and str(request.POST['fecha_hasta'])=='':
		# filtro+=" UNION SELECT * FROM dt_repo_horas Where complejo_id="+ str(request.POST['complejo_id'])
		# filtro+=" AND fecha_ingreso is null"

	str_query = "SELECT * FROM dt_repo_horas" + filtro
	##print  str_query
	cursor = connection.cursor()
	cursor.execute(str_query)
	qs = cursor.fetchall()
	####print   qs
	qs_alquiler= TipoAlquiler.objects.all().order_by('nombre')
	####print   qs_alquiler
	tuples_resultado=[]
	for item in qs:
		###print   "\n -->",item
		#verifica que no exista alguna tupla con sus datos 
		if verificar_existencia(item,tuples_resultado):
			for tipo_a in qs_alquiler:
				#cancha id, complejo id, tipo alquiler id, nombre cancha, tipo alquiler nombre, cant horas
				if item[6] is None:
					cant_inst=item[7]
				else:
					cant_inst=time_to_int(item[6])
				tupla_aux= [int(item[0]),int(item[1]),int(tipo_a.tipo_alquiler_id),str(item[4]),str(tipo_a.nombre),0,cant_inst]
				tuples_resultado.append(tupla_aux)


	for item in qs:
		for tupla in tuples_resultado:
			if item[2] is not None:
				if int(item[0])==int(tupla[0]) and int(item[1])==int(tupla[1]) and int(item[2])==int(tupla[2]):
					####print   "\n -->",time_to_int(item[5])
					tupla[5]+=time_to_int(item[5])
					total_horas_usadas+=time_to_int(item[5])

	lista_resultado=[]				
#-------------------------------------------------------------------------------------------
	filtro_horas=" WHERE 1=1"
	if 'complejo_id' in request.POST.keys() and str(request.POST['complejo_id'])!='':
		filtro_horas+=" AND complejo_id = " + str(request.POST['complejo_id'])

	str_query = "SELECT * FROM dt_repo_horasposibles" + filtro_horas
	cursor = connection.cursor()
	cursor.execute(str_query)
	repo_horas = cursor.fetchall()
	for hora in repo_horas:
		##print  "\n",hora
		total_horas_posibles+=time_to_int(hora[2])/7
#--------------------------------------------------------------------------------------------
	for item in tuples_resultado:
		##print  item
		##print  '\n'
		item.append(total_horas_posibles)
		item.append(total_horas_usadas)
		####print   "\n",item
		lista_resultado.append(tuple(item))

	##print  "RES", lista_resultado
	return lista_resultado

	####print   "\n TOTAL HORAS POSIBLES --> ", total_horas_posibles
	####print   "\n TOTAL HORAS USADAS -->",total_horas_usadas

def obtener_div_horas(request):
	html=get_html_reporteHoras(ReporteHorasCancha(request),request)
	return HttpResponse(json.dumps({'html':html}), content_type='application/json')

def get_html_reporteHoras(rows,request):
	qs_alquiler= TipoAlquiler.objects.all().order_by('nombre')
	###print  "-------------------- GET HTML ---------------------"
	###print  "\n"
	#for r in rows:
		##print  "\n",r
	###print  "cantidad de alquiler", len(qs_alquiler)
	###print  "cantidad de rows", len(rows)
	if 'fecha_desde' in request.POST.keys() and 'fecha_hasta' in request.POST.keys():
		##print  "TRAE DIAS"
		dic_dias= calcular_horas_posibles(request)
		##print  dic_dias
	if 'errors' in dic_dias.keys():
		cant_dias=0
	else:
		cant_dias= abs(dic_dias['resultado'])
	###print  "cantidad de dias", cant_dias
	total_canchas= len(rows)//len(qs_alquiler)
	#lista_nombre_alquiler=[]
	##print  "-------------------- HTML --------------------------"
	contador_auxiliar=0
	cadena=''

	if len(rows)==0:
		return cadena

	##print  total_canchas
	##print  "total_canchas//3--->", float(total_canchas)/3
	##print  "total_canchas//3 ceil --->", math.ceil(float(total_canchas)/3)
	for i in range(int(math.ceil(float(total_canchas)/3))):#porque va a ir de 3 en 3
		##print  "----------------- "+str(i)+" -----------------------"
		cadena+="<div class='row'>"
		cadena+="<div class='col-sm-3'>"
		
		cadena+="<table class='table table-bordered table-hover table-striped'>"
		#se llena la lista con nombres de alquiler
		cadena+="<tr class='success'><td>Cancha</td></tr>"
		cadena+="<tr class='success'><td>&nbsp;</td></tr>"
		cadena+="<tr class='warning'><td>&nbsp;</td></tr>"
		for alqui in qs_alquiler:
			cadena+="<tr class='info'><td>"+str(alqui.nombre)+"</td></tr>"
		cadena+="</table>"
		cadena+="</div>"
		try:
			for k in range(3): 
				for j in range(len(qs_alquiler)):
					##print  "\n\t-------------- "+str(j)+"------------------"
					##print  "\t\t--->",rows[contador_auxiliar]
					row=rows[contador_auxiliar] 
					if j==0:
						total_horas_posibles= contar_horas(rows[contador_auxiliar:contador_auxiliar+len(qs_alquiler)])
						cadena+="<div class='col-sm-3'>"
						cadena+="<table class='table table-bordered table-hover table-striped'>"
						try:
							nbr_complejo= Complejo.objects.get(complejo_id=int(row[1]))
							cadena+="<tr><td class='success' colspan='2'><p class='text-success'><strong>"+row[3]+"</strong></p><p class='small text-right'><small><i class='fa fa-flag'></i>&nbsp;"+nbr_complejo.nombre+"</small></p>"+"</td></tr>"
						except:
							cadena+="<tr><td class='success' colspan='2'><p class='text-success'><strong>"+row[3]+"</strong></p></td></tr>"
						cadena+="<tr><td class='warning'>Horas</td><td class='warning'>%</td>"
					if total_horas_posibles!=0:
							porcen= truncate((float(row[5])/float(total_horas_posibles))*100,3)
					else:
							porcen= truncate((float(row[5])/float(1))*100,3)
					cadena+="<tr><td>"+str(row[5])+"</td><td>"+str(porcen)+"% </td></tr>"
					if j==len(qs_alquiler)-1:
						cadena+="<tr class='default'><td>&nbsp;</td></tr>"
						capacidad_inst= truncate(float(float(float(row[6])/7)*float(cant_dias)),3)
						cadena+="<tr><td class='info'>Capacidad instalada</td><td class='warning capacidad_instalada'>"+str(capacidad_inst)+"</td>"
						cadena+="<tr><td class='info'>Horas usadas</td><td class='warning horas_usadas'>"+str(total_horas_posibles)+"</td>"
						if capacidad_inst!=0:
							uso= truncate(total_horas_posibles/capacidad_inst,3)*float(100)
						else:
							uso= 0
						cadena+="<tr><td class='info'>% de uso</td><td class='warning'>"+str(uso)+" % </td>"
						cadena+="</table>"
						cadena+="</div>"
					contador_auxiliar=contador_auxiliar+1
		except:
			pass

		cadena+="</div>"
	return cadena

def truncate(number, digits):
    stepper = pow(10.0, digits)
    return math.trunc(stepper * number) / stepper

def contar_horas(lista):
	##print  "L I S T A ->",lista
	suma= float(0)
	for item in lista:
		suma+=float(item[5])
	return suma

def ReporteHorasCanchaData(request):
	fetch=convert_fetchall(ReporteHorasCancha(request))
	###print  get_html_reporteHoras(ReporteHorasCancha(request))
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
		###print   arr_hasta
		arr_desde= request.POST['fecha_desde'].split('-')
		#d0 = date(int(arr_desde[0]), int(arr_desde[1]), int(arr_desde[2]))
		####print   d0
		#d1 = date(int(arr_hasta[0]), int(arr_hasta[1]), int(arr_desde[2]))
		d0=datetime.strptime(str(request.POST['fecha_desde']), "%Y-%m-%d").date()
		d1=datetime.strptime(str(request.POST['fecha_hasta']), "%Y-%m-%d").date()
		delta = d0 - d1
		cantidad_dias= delta.days-1
		##print   "Cantidad de dias-->",cantidad_dias
		if cantidad_dias < 0: #esta bien :3
			#resultado= float(request.POST['horas_posibles'])*(-1*cantidad_dias)
			resultado=cantidad_dias
			####print   resultado
			fetch={'resultado':resultado}
		elif cantidad_dias==0:	#tambien esta bien
			#resultado= float(request.POST['horas_posibles'])
			resultado=0
			fetch={'resultado':resultado}
		else: #no esta bien :c
			fetch={'errors':1}
	except:
		fetch={'errors':1}
	return fetch

def TopClientesData(request):
	filtro=""
	if str(request.POST['fecha_desde'])!= '':
		filtro+=" AND r.fecha_ingreso >= '" + str(request.POST['fecha_desde']) + "'" 

	if str(request.POST['fecha_hasta'])!='':
		filtro+=" AND r.fecha_ingreso <= '" + str(request.POST['fecha_hasta']) + "'"
#COALESCE(to_char(recan.precio_acordado, '9G999.99'::text), to_char(0, '9G999.99'::text))
	if 'complejo_id' in request.POST.keys() and str(request.POST['complejo_id']) !='':
		filtro+=" AND can.complejo_id="+str(request.POST['complejo_id'])

	str_query = "SELECT c.nombre,c.telefono,c.correo,\
				'$ '|| COALESCE(to_char(\
				(SELECT sum(res.precio) from modulo_1_reserva res\
				where res.cliente_id=c.cliente_id)\
				, '9G999.99'), to_char(0, '9G999.99')) as precio_total,\
				c.cliente_id\
				FROM modulo_1_reserva r\
				INNER JOIN modulo_1_cliente c ON c.cliente_id=r.cliente_id\
				LEFT JOIN modulo_1_reservacancha rc ON rc.reserva_id=r.reserva_id\
				LEFT JOIN modulo_1_cancha can ON can.cancha_id=rc.cancha_id	\
				WHERE r.empresa_id is null" + filtro
	str_query+=" GROUP BY c.cliente_id,c.nombre,c.telefono,c.correo \
				ORDER BY precio_total DESC\
				LIMIT 5"
	#print "\n\n",str_query
	cursor = connection.cursor()
	cursor.execute(str_query)
	qs = cursor.fetchall()

	return HttpResponse(json.dumps(convert_fetchall(qs)), content_type='application/json')

def TopEmpresaData(request):
	filtro=""
	if str(request.POST['fecha_desde'])!= '':
		filtro+=" AND r.fecha_ingreso >= '" + str(request.POST['fecha_desde']) + "'" 

	if str(request.POST['fecha_hasta'])!='':
		filtro+=" AND r.fecha_ingreso <= '" + str(request.POST['fecha_hasta']) + "'"

	if 'complejo_id' in request.POST.keys() and str(request.POST['complejo_id']) !='':
		filtro+=" AND can.complejo_id="+str(request.POST['complejo_id'])

	str_query = "SELECT c.nombre,c.contacto,c.telefono_contacto,\
				'$ '|| COALESCE(to_char(\
				(SELECT sum(res.precio) from modulo_1_reserva res\
				where res.empresa_id=c.empresa_id)\
				, '9G999.99'), to_char(0, '9G999.99')) as precio_total,\
				c.empresa_id\
				FROM modulo_1_reserva r \
				INNER JOIN modulo_1_empresa c ON c.empresa_id=r.empresa_id\
				LEFT JOIN modulo_1_reservacancha rc ON rc.reserva_id=r.reserva_id\
				LEFT JOIN modulo_1_cancha can ON can.cancha_id=rc.cancha_id	\
				WHERE r.cliente_id is null  " + filtro
	str_query+=" GROUP BY c.nombre,c.contacto,c.telefono_contacto,c.empresa_id \
				ORDER BY precio_total DESC\
				LIMIT 5"
	cursor = connection.cursor()
	cursor.execute(str_query)
	qs = cursor.fetchall()
	####print   convert_fetchall(qs)
	return HttpResponse(json.dumps(convert_fetchall(qs)), content_type='application/json')

def convert_fetchall_top(cursor):
	dict_cursor={}
	list_aux=[]
	for item in cursor:
		list_aux.append([item[0],item[1],item[2],time_to_int(item[3]),item[4]])
	dict_cursor['recordsTotal']=len(list_aux)
	dict_cursor['recordsFiltered']=len(list_aux)
	dict_cursor['draw']= len(list_aux)//10
	dict_cursor['data']=list_aux
	return dict_cursor