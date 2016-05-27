from django.shortcuts import render
from funciones_generales import convert_fetchall
from django.db import connection
from django.http import HttpResponse
from modulo_1.forms import ComplejoForm
from modulo_1.models import Complejo
import json
import hashlib

def RegistroComplejo(request):
	data={
		'form_complejo': ComplejoForm(),
	}
	return render(request,'registrocomplejo.html',data)

def ComplejoData(request):
	str_query = "SELECT complejo_id,nombre from modulo_1_complejo"
	cursor = connection.cursor()
	cursor.execute(str_query)
	qs = cursor.fetchall()
	clientes = convert_fetchall(qs)
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