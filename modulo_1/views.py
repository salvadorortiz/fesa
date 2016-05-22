# -*- encoding: utf-8 -*-

from django.shortcuts import render
from funciones_generales import convert_fetchall
from django.db import connection
from django.http import HttpResponse
from .models import Cancha,Usuario
from modulo_1.forms import UsuarioForm
import json
import hashlib
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def Autenticacion(request):
	usuario= Usuario.objects.filter(usuario=request.POST['user'], password=hashlib.sha1(request.POST['pass']).hexdigest(), estado=True)
	if(len(usuario)==1):
		respuesta=json.dumps({'error':False})
		request.session['user_log']=request.POST['user']
		request.session['type_user']=usuario[0].tipo_usuario
	else:
		respuesta=json.dumps({'error':True})
	return HttpResponse(respuesta,content_type='application/json')

def PreciosView(request):
	return render(request,'precios.html')

def dt_precios(request):
	str_query = """SELECT ca.cancha_id,
				   co.nombre AS nombre_complejo,
				   ca.nombre AS nombre_cancha,
				   '$'::text || ca.precio::text AS precio
				   FROM modulo_1_cancha ca
				   JOIN modulo_1_complejo co ON ca.complejo_id = co.complejo_id"""
	cursor = connection.cursor()
	cursor.execute(str_query)
	qs = cursor.fetchall()
	canchas_lista = convert_fetchall(qs)
	return HttpResponse(json.dumps(canchas_lista), content_type='application/json')

def GuardarPrecio(request):
	Cancha.objects.filter(cancha_id=request.POST['id_cancha']).update(precio=request.POST['precio'])
	return HttpResponse(json.dumps({}), content_type='application/json')

def RegistroUsuarioView(request):
	data={'usuario_form': UsuarioForm()}
	return render(request,'usuarios.html',data)

def dt_usuarios(request):
	str_query = """SELECT usuario_id,nombre,usuario,area,jefe_directo,
					CASE tipo_usuario
						WHEN 'A'::text THEN 'Tipo A'
						WHEN 'B'::text THEN 'Tipo B'
						WHEN 'R'::text THEN 'Administrador'
					END AS tipo,
					CASE estado
						WHEN true THEN '<center><i class="fa fa-check"></i></center>'
						WHEN false THEN '<center><i class="fa fa-times"></i></center>'
					END AS estado,
					password
					FROM modulo_1_usuario"""
	cursor = connection.cursor()
	cursor.execute(str_query)
	qs = cursor.fetchall()
	clientes = convert_fetchall(qs)
	return HttpResponse(json.dumps(clientes), content_type='application/json')

def GuardarUsuario(request):
	queryDict_ =  request.POST.copy()
	queryDict_.__setitem__('password', hashlib.sha1(queryDict_.__getitem__('password')).hexdigest())
	
	form_usuario = UsuarioForm(queryDict_ or None)
	if form_usuario.is_valid():
		form_usuario.save()
		return HttpResponse(json.dumps({}), content_type='application/json')
	else:
		return HttpResponse(json.dumps({'errors': form_usuario.errors}), content_type='application/json')

def GuardarCambiosUsuario(request):
	form_usuario=UsuarioForm(request.POST or None)
	if form_usuario.is_valid():
		obj_usuario= Usuario.objects.get(usuario_id=int(request.POST['usuario_id']))
		obj_usuario.area=str(request.POST['area'])
		obj_usuario.jefe_directo= str(request.POST['jefe_directo'])
		obj_usuario.nombre = str(request.POST['nombre'])
		obj_usuario.usuario= str(request.POST['usuario'])
		obj_usuario.password = hashlib.sha1(request.POST['password']).hexdigest()
		if request.POST['estado_usuario'] == "false":
			obj_usuario.estado= False
		else:
			obj_usuario.estado= True

		obj_usuario.tipo_usuario = str(request.POST['tipo_usuario'])
		obj_usuario.save(force_update=True)
		return HttpResponse(json.dumps({}), content_type='application/json')
	else:
		return HttpResponse(json.dumps({'errors': form_usuario.errors}), content_type='application/json')