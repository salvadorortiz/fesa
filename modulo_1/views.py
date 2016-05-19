from django.shortcuts import render
from funciones_generales import convert_fetchall
from django.db import connection
from django.http import HttpResponse
from .models import Cancha
import json

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