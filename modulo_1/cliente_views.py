from django.shortcuts import render
from funciones_generales import convert_fetchall
from django.db import connection
from django.http import HttpResponse
from modulo_1.forms import ClienteForm, EmpresaForm
from modulo_1.models import Cliente
import json
import hashlib

def RegistroClienteView(request):
	data={'cliente_form': ClienteForm()}
	return render(request,'registrocliente.html',data)

def GuardarCliente(request):
	form_cliente=ClienteForm(request.POST or None)
	if form_cliente.is_valid():
		form_cliente.save()
		return HttpResponse(json.dumps({}), content_type='application/json')
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
		return HttpResponse(json.dumps({}), content_type='application/json')
	else:
		return HttpResponse(json.dumps({'errors': form_cliente.errors}), content_type='application/json')

def RegistroEmpresaView(request):
	data={'empresa_form': EmpresaForm()}
	return render(request,'registroempresa.html',data)