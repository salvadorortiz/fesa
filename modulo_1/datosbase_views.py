#-*- coding: utf-8 -*-
from django.shortcuts import render
from funciones_generales import convert_fetchall, time_in_range
from django.db import connection
from django.http import HttpResponse
from modulo_1.forms import ComplejoForm,CanchaForm,HorarioCanchaForm
from modulo_1.models import Complejo,Cancha,PrecioXCancha
from datetime import datetime
import json
import hashlib

def RegistroComplejo(request):
	if not request.session.has_key('user_log'):
		return render(request,'login.html')
	data={
		'form_complejo': ComplejoForm(),
		'form_horario': HorarioCanchaForm(),
		'form_cancha': CanchaForm(),
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
	errores={}
	if request.POST['hora_cierre'] == '':
		errores.update({'hora_cierre': ['Es un campo obligatorio']})
	if request.POST['hora_apertura'] == '':
		errores.update({'hora_apertura': ['Es un campo obligatorio']})
	if 'dia' not in request.POST.keys():
		errores.update({'dia': ['Es un campo obligatorio']})

	if errores=={}:
		print request.POST['dias']
		
		apertura= datetime.strptime(str(request.POST['hora_apertura']), '%H:%M').time()
		cierre= datetime.strptime(str(request.POST['hora_cierre']), '%H:%M').time()

		for dia in request.POST['dias'].split(','):
			flag=True
			arr_horarios= PrecioXCancha.objects.filter(cancha_id=int(request.POST['cancha']))
			for horario in arr_horarios:
				if str(dia) == str(horario.dia):
					if horario.hora_apertura==apertura and horario.hora_cierre==cierre:
						flag=False
					if time_in_range(horario.hora_apertura, horario.hora_cierre, apertura) is True:
						flag=False
					if time_in_range(horario.hora_apertura, horario.hora_cierre, cierre) is True:
						flag=False

			if flag is True:
				obj_preciocancha=PrecioXCancha()
				obj_preciocancha.cancha= Cancha.objects.get(cancha_id=int(request.POST['cancha']))
				obj_preciocancha.hora_apertura=apertura
				obj_preciocancha.hora_cierre=cierre
				obj_preciocancha.dia= str(dia)
				obj_preciocancha.save()
		
		return HttpResponse(json.dumps({}), content_type='application/json')
	else:
		return HttpResponse(json.dumps({'errors': errores}), content_type='application/json')

def CargarHorario(request):
	obj_preciocancha=PrecioXCancha.objects.get(precio_cancha_id=int(request.POST['id_preciocancha']))
	respuesta={
		'id_preciocancha': int(obj_preciocancha.precio_cancha_id),
		'dia': str(obj_preciocancha.dia),
		'hora_apertura': obj_preciocancha.hora_apertura.strftime("%H:%M"),
		'hora_cierre': obj_preciocancha.hora_cierre.strftime("%H:%M"),
	}
	return HttpResponse(json.dumps(respuesta), content_type='application/json')

def GuardarCambiosHorario(request):
	errores={}
	if request.POST['hora_cierre'] == '':
		errores.update({'hora_cierre': ['Es un campo obligatorio']})
	if request.POST['hora_apertura'] == '':
		errores.update({'hora_apertura': ['Es un campo obligatorio']})
	
	if errores=={}:
		
		apertura= datetime.strptime(str(request.POST['hora_apertura']), '%H:%M').time()
		cierre= datetime.strptime(str(request.POST['hora_cierre']), '%H:%M').time()

		flag=True
		arr_horarios= PrecioXCancha.objects.filter(cancha_id=int(request.POST['cancha']))
		for horario in arr_horarios:
			if str(request.POST['dia']) == str(horario.dia):
				if horario.hora_apertura==apertura and horario.hora_cierre==cierre:
					flag=False
				if time_in_range(horario.hora_apertura, horario.hora_cierre, apertura) is True:
					flag=False
				if time_in_range(horario.hora_apertura, horario.hora_cierre, cierre) is True:
					flag=False

		if flag is True:
			obj_preciocancha=PrecioXCancha.objects.get(precio_cancha_id=int(request.POST['id_preciocancha']))
			obj_preciocancha.cancha= Cancha.objects.get(cancha_id=int(request.POST['cancha']))
			obj_preciocancha.hora_apertura=apertura
			obj_preciocancha.hora_cierre=cierre
			obj_preciocancha.dia= str(request.POST['dia'])
			obj_preciocancha.save(force_update=True)
	
		return HttpResponse(json.dumps({}), content_type='application/json')
	else:
		return HttpResponse(json.dumps({'errors': errores}), content_type='application/json')
	
def EliminarHorarioCancha(request):
	PrecioXCancha.objects.filter(precio_cancha_id=int(request.POST['id_preciocancha'])).delete()
	return HttpResponse(json.dumps({}), content_type='application/json')
	
def HorarioComplejoData(request):
	print "entro"
	if str(request.POST['cancha_id']) =="":
		complejo= ' WHERE cancha_id=0'
	else:
		complejo= ' WHERE cancha_id='+str(request.POST['cancha_id'])
	str_query = "SELECT precio_cancha_id,dia,CASE\
					when dia='X' THEN 'Lunes-Viernes'\
					when dia='S' THEN 'Sábado'\
					when dia='D' THEN 'Domingo'\
					END AS dia_semena,\
					to_char(hora_apertura, 'HH24:MI') AS hora_apertura,\
					to_char(hora_cierre, 'HH24:MI') As hora_cierre\
					from modulo_1_precioxcancha"+complejo
	cursor = connection.cursor()
	cursor.execute(str_query)
	qs = cursor.fetchall()
	#print qs
	clientes = convert_fetchall(qs)
	return HttpResponse(json.dumps(clientes), content_type='application/json')

def CanchaData(request):
	if str(request.POST['complejo_id']) =="":
		complejo= ' WHERE complejo_id=0'
	else:
		complejo= ' WHERE complejo_id='+str(request.POST['complejo_id'])
	str_query = "SELECT cancha_id,complejo_id,nombre\
					from modulo_1_cancha"+complejo
	cursor = connection.cursor()
	cursor.execute(str_query)
	qs = cursor.fetchall()
	#print qs
	clientes = convert_fetchall(qs)
	return HttpResponse(json.dumps(clientes), content_type='application/json')

def GuardarCancha(request):
	form_cancha=CanchaForm(request.POST or None)
	if form_cancha.is_valid():
		form_cancha.save()
		return HttpResponse(json.dumps({}), content_type='application/json')
	else:
		return HttpResponse(json.dumps({'errors': form_cancha.errors}), content_type='application/json')

def GuardarCambiosCancha(request):
	form_cancha=CanchaForm(request.POST or None)
	if form_cancha.is_valid():
		#form_cancha.save()
		obj_cancha= Cancha.objects.get(cancha_id=int(request.POST['cancha']))
		obj_cancha.nombre=str(request.POST['nombre'])
		obj_cancha.horas_posibles= int(request.POST['horas_posibles'])
		obj_cancha.save(force_update=True)
		return HttpResponse(json.dumps({}), content_type='application/json')
	else:
		return HttpResponse(json.dumps({'errors': form_cancha.errors}), content_type='application/json')

def CargarCancha(request):
	obj_cancha=Cancha.objects.filter(cancha_id=int(request.POST['id_cancha'])).values_list('cancha_id','nombre','horas_posibles')
	lista_resultado=[]
	print obj_cancha
	for cancha in obj_cancha:
		lista_resultado+=list(cancha)
	return HttpResponse(json.dumps({'cancha': lista_resultado}), content_type='application/json')


def EliminarCancha(request):
	print "entro :)"
	Cancha.objects.filter(cancha_id=int(request.POST['id_cancha'])).delete()
	return HttpResponse(json.dumps({}), content_type='application/json')
