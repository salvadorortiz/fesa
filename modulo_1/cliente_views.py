#-*- coding: utf-8 -*-
from django.shortcuts import render
from funciones_generales import convert_fetchall
from django.db import connection
from django.http import HttpResponse
from modulo_1.forms import ClienteForm, EmpresaForm
from modulo_1.models import Cliente, Empresa
import json
import hashlib
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def RegistroClienteView(request):
	codigo_cliente= Cliente.objects.count()+1
	data={'cliente_form': ClienteForm(initial={'codigo': codigo_cliente,'ingresado_por': request.session['user_log']})}
	return render(request,'registrocliente.html',data)

def GuardarCliente(request):
	form_cliente=ClienteForm(request.POST or None)
	if form_cliente.is_valid():
		form_cliente.save()
		codigo_cliente= Cliente.objects.count()+1
		return HttpResponse(json.dumps({'codigo': codigo_cliente}), content_type='application/json')
	else:
		return HttpResponse(json.dumps({'errors': form_cliente.errors}), content_type='application/json')
	
def dt_clientes(request):
	str_query = "SELECT cliente_id,codigo,nombre,telefono,correo from modulo_1_cliente"
	cursor = connection.cursor()
	cursor.execute(str_query)
	qs = cursor.fetchall()
	clientes = convert_fetchall(qs)
	return HttpResponse(json.dumps(clientes), content_type='application/json')

def CargarCliente(request):
	obj_cliente=Cliente.objects.filter(cliente_id=int(request.POST['id_cliente'])).values_list('cliente_id','codigo','nombre','direccion','DUI','telefono','telefono_alterno','correo')
	print obj_cliente
	lista_resultado=[]
	for cliente in obj_cliente:
		lista_resultado+=list(cliente)
	return HttpResponse(json.dumps({'cliente': lista_resultado}), content_type='application/json')

def GuardarCambiosCliente(request):
	form_cliente=ClienteForm(request.POST or None)
	if form_cliente.is_valid():
		#form_cliente.save()
		obj_cliente= Cliente.objects.get(cliente_id=int(request.POST['id_cliente']))
		obj_cliente.codigo=str(request.POST['codigo'])
		obj_cliente.nombre= str(request.POST['nombre'])
		obj_cliente.direccion = str(request.POST['direccion'])
		obj_cliente.telefono= str(request.POST['telefono'])
		obj_cliente.telefono_alterno = str(request.POST['telefono_alterno'])
		obj_cliente.DUI= str(request.POST['DUI'])
		obj_cliente.correo = str(request.POST['correo'])
		obj_cliente.save(force_update=True)
		codigo_cliente= Cliente.objects.count()+1
		return HttpResponse(json.dumps({'codigo': codigo_cliente}), content_type='application/json')
	else:
		return HttpResponse(json.dumps({'errors': form_cliente.errors}), content_type='application/json')

def RegistroEmpresaView(request):
	codigo_empresa= Empresa.objects.count()+1
	data={'empresa_form': EmpresaForm(initial={'codigo':codigo_empresa,'ingresado_por': request.session['user_log']})}
	return render(request,'registroempresa.html',data)

def dt_empresas(request):
	str_query = "SELECT empresa_id,codigo,nombre,telefono,contacto,correo_contacto from modulo_1_empresa"
	cursor = connection.cursor()
	cursor.execute(str_query)
	qs = cursor.fetchall()
	clientes = convert_fetchall(qs)
	return HttpResponse(json.dumps(clientes), content_type='application/json')

def GuardarEmpresa(request):
	form_empresa=EmpresaForm(request.POST or None)
	if form_empresa.is_valid():
		form_empresa.save()
		codigo_empresa= Empresa.objects.count()+1
		return HttpResponse(json.dumps({'codigo': codigo_empresa}), content_type='application/json')
	else:
		return HttpResponse(json.dumps({'errors': form_empresa.errors}), content_type='application/json')

def CargarEmpresa(request):
	obj_empresa=Empresa.objects.filter(empresa_id=int(request.POST['id_empresa'])).values_list('empresa_id','codigo','nombre','nit','registro_iva','telefono','contacto','telefono_contacto','correo_contacto')
	lista_resultado=[]
	for empresa in obj_empresa:
		lista_resultado+=list(empresa)
	return HttpResponse(json.dumps({'cliente': lista_resultado}), content_type='application/json')

def GuardarCambiosEmpresa(request):
	form_empresa=EmpresaForm(request.POST or None)
	if form_empresa.is_valid():
		#form_cliente.save()
		obj_empresa= Empresa.objects.get(empresa_id=int(request.POST['id_empresa']))
		obj_empresa.codigo=str(request.POST['codigo'])
		obj_empresa.nombre= str(request.POST['nombre'])
		obj_empresa.nit = str(request.POST['nit'])
		obj_empresa.registro_iva = str(request.POST['registro_iva'])
		obj_empresa.telefono= str(request.POST['telefono'])
		obj_empresa.contacto = str(request.POST['contacto'])
		obj_empresa.telefono_contacto= str(request.POST['telefono_contacto'])
		obj_empresa.correo_contacto = str(request.POST['correo_contacto'])
		obj_empresa.save(force_update=True)
		codigo_empresa= Empresa.objects.count()+1
		return HttpResponse(json.dumps({'codigo': codigo_empresa}), content_type='application/json')
	else:
		return HttpResponse(json.dumps({'errors': form_empresa.errors}), content_type='application/json')