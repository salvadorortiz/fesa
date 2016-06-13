#-*- coding: utf-8 -*-
from django.shortcuts import render
from funciones_generales import convert_fetchall
from django.db import connection
from django.http import HttpResponse
from modulo_1.forms import ClienteForm, EmpresaForm
from modulo_1.models import Cliente, Empresa,Complejo
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
	data={'cmb_complejo':cmb_complejo}
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