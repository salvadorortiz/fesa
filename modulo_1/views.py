from django.shortcuts import render
from funciones_generales import convert_fetchall
from django.db import connection
from django.http import HttpResponse
from .models import Cancha,Usuario
import json
import hashlib

def Autenticacion(request):
	usuario= Usuario.objects.filter(user=request.POST['user'], password=hashlib.sha1(request.POST['pass']).hexdigest())
	if(len(usuario)==1):
		respuesta=json.dumps({'error':False})
		request.session['user_log']=request.POST['user']
	else:
		respuesta=json.dumps({'error':True})
	return HttpResponse(respuesta,content_type='application/json')

def PreciosView(request):
	return render(request,'precios.html')

def dt_vista_precios(request):
	str_query = "SELECT * FROM dt_vista_precios"
	cursor = connection.cursor()
	cursor.execute(str_query)
	qs = cursor.fetchall()
	canchas_lista = convert_fetchall(qs)
	return HttpResponse(json.dumps(canchas_lista), content_type='application/json')

def GuardarPrecio(request):
	Cancha.objects.filter(cancha_id=request.POST['id_cancha']).update(precio=request.POST['precio'])
	return HttpResponse(json.dumps({}), content_type='application/json')