#-*- coding: utf-8 -*-
from django.shortcuts import render
from funciones_generales import convert_fetchall
from django.db import connection
from django.http import HttpResponse
from modulo_1.forms import ComplejoForm, HorarioForm
from modulo_1.models import Complejo,HorarioComplejo
from datetime import datetime
import json
import hashlib

def RegistroComplejo(request):
	data={
		'form_complejo': ComplejoForm(),
		'form_horario': HorarioForm(),
	}
	return render(request,'registrocomplejo.html',data)

def ComplejoData(request):
	str_query = "SELECT complejo_id,nombre from modulo_1_complejo"
	cursor = connection.cursor()
	cursor.execute(str_query)
	qs = cursor.fetchall()
	clientes = convert_fetchall(qs)
	#print clientes
	return HttpResponse(json.dumps(clientes), content_type='application/json')

def GuardarComplejo(request):
	form_complejo=ComplejoForm(request.POST or None)
	if form_complejo.is_valid():
		form_complejo.save()
		return HttpResponse(json.dumps({}), content_type='application/json')
	else:
		return HttpResponse(json.dumps({'errors': form_complejo.errors}), content_type='application/json')

def GuardarCambiosComplejo(request):
	form_complejo=ComplejoForm(request.POST or None)
	if form_complejo.is_valid():
		obj_complejo= Complejo.objects.get(complejo_id=int(request.POST['id_complejo']))
		obj_complejo.nombre= str(request.POST['nombre'])
		obj_complejo.direccion= str(request.POST['direccion'])
		obj_complejo.save(force_update=True)
		return HttpResponse(json.dumps({}), content_type='application/json')
	else:
		return HttpResponse(json.dumps({'errors': form_complejo.errors}), content_type='application/json')

def CargarComplejo(request):
	obj_complejo=Complejo.objects.filter(complejo_id=int(request.POST['id_complejo'])).values_list('complejo_id','nombre','direccion')
	lista_resultado=[]
	for complejo in obj_complejo:
		lista_resultado+=list(complejo)
	return HttpResponse(json.dumps({'complejo': lista_resultado}), content_type='application/json')

def GuardarHorario(request):
	dias=request.POST['cadena'].split('||')
	print dias
	HorarioComplejo.objects.filter(complejo_id=int(request.POST['complejo_id'])).delete()
	for dia in dias:
		arr= dia.split(',')
		if len(arr) == 3:
				obj_horario=HorarioComplejo()
				obj_horario.complejo_id=int(request.POST['complejo_id'])
				obj_horario.hora_apertura=datetime.strptime(str(arr[1]), '%H:%M').time()
				obj_horario.hora_cierre= datetime.strptime(str(arr[2]), '%H:%M').time()
				obj_horario.dia=str(arr[0])
				obj_horario.save()
			#print '\t',arr
			#print datetime.strptime(str(arr[1]), '%H:%M%p').time()
	return HttpResponse(json.dumps({}), content_type='application/json')

def HorarioComplejoData(request):
	print "entro"
	if str(request.POST['complejo_id']) =="":
		complejo= ' WHERE complejo_id=0'
	else:
		complejo= ' WHERE complejo_id='+str(request.POST['complejo_id'])
	str_query = "SELECT complejo_id,dia,CASE\
					when dia='L' THEN 'Lunes'\
					when dia='M' THEN 'Martes'\
					when dia='X' THEN 'Miércoles'\
					when dia='J' THEN 'Jueves'\
					when dia='V' THEN 'Viernes'\
					when dia='S' THEN 'Sábado'\
					when dia='D' THEN 'Domingo'\
					END AS dia_semena,\
					to_char(hora_apertura, 'HH24:MI') AS hora_apertura,\
					to_char(hora_cierre, 'HH24:MI') As hora_cierre\
					from modulo_1_horariocomplejo"+complejo
	cursor = connection.cursor()
	cursor.execute(str_query)
	qs = cursor.fetchall()
	#print qs
	clientes = convert_fetchall(qs)
	return HttpResponse(json.dumps(clientes), content_type='application/json')