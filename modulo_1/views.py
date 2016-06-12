# -*- encoding: utf-8 -*-

from django.shortcuts import render
from funciones_generales import convert_fetchall
from django.db import connection
from django.http import HttpResponse
from .models import Cancha,Usuario,FormaPago,FormaFacturacion,TipoAlquiler,PrecioXCancha,Reserva,Cliente,Empresa,Complejo,ReservaCancha
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
	str_query = """SELECT 
					 ca.cancha_id
					,pc.precio_cancha_id
					,co.complejo_id
					,co.nombre AS nombre_complejo
					,ca.nombre AS nombre_cancha
					,CASE pc.dia
						WHEN 'X' THEN 'Lunes-Viernes'::text
						WHEN 'S' THEN 'Sábado'::text
						WHEN 'D' THEN 'Domingo'::text
					 END AS días
					,pc.hora_apertura::text AS hora_apertura
					,pc.hora_cierre::text AS hora_cierre
					,'$'::text || pc.precio::text AS precio
				FROM 	modulo_1_cancha ca
				JOIN 	modulo_1_complejo co ON co.complejo_id = ca.complejo_id AND co.complejo_id ="""+ request.POST['complejo_id']+"""
				JOIN modulo_1_precioxcancha pc ON pc.cancha_id = ca.cancha_id GROUP BY ca.cancha_id,pc.precio_cancha_id,co.complejo_id"""
	cursor = connection.cursor()
	cursor.execute(str_query)
	qs = cursor.fetchall()
	canchas_lista = convert_fetchall(qs)
	return HttpResponse(json.dumps(canchas_lista), content_type='application/json')

def GuardarPrecio(request):
	PrecioXCancha.objects.filter(precio_cancha_id=request.POST['precio_cancha_id']).update(precio=request.POST['precio'])
	return HttpResponse(json.dumps({}), content_type='application/json')

def RegistroUsuarioView(request):
	data={'usuario_form': UsuarioForm()}
	return render(request,'usuarios.html',data)

def dt_usuarios(request):
	str_query = """SELECT usuario_id,nombre,usuario,area,jefe_directo,
					CASE tipo_usuario
						WHEN 'A'::text THEN 'A'
						WHEN 'B'::text THEN 'B'
						WHEN 'R'::text THEN 'Administrador'
					END AS tipo,
					CASE estado
						WHEN true THEN '<center><p class="text-success">Activo</p></center>'
						WHEN false THEN '<center><p class="text-danger">Inactivo</p></center>'
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
		if obj_usuario.password != request.POST['password']:
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

def CatalogosView(request):
	return render(request,'catalogos.html')

def dt_forma_pago(request):
	str_query = "SELECT * FROM modulo_1_formapago"
	cursor = connection.cursor()
	cursor.execute(str_query)
	qs = cursor.fetchall()
	forma_pago = convert_fetchall(qs)
	return HttpResponse(json.dumps(forma_pago), content_type='application/json')

def dt_forma_facturacion(request):
	str_query = "SELECT * FROM modulo_1_formafacturacion"
	cursor = connection.cursor()
	cursor.execute(str_query)
	qs = cursor.fetchall()
	forma_facturacion = convert_fetchall(qs)
	return HttpResponse(json.dumps(forma_facturacion), content_type='application/json')

def dt_alquiler(request):
	str_query = "SELECT * FROM modulo_1_tipoalquiler"
	cursor = connection.cursor()
	cursor.execute(str_query)
	qs = cursor.fetchall()
	tipo_alquiler = convert_fetchall(qs)
	return HttpResponse(json.dumps(tipo_alquiler), content_type='application/json')

def GuardarCatalogo(request):
	if request.POST['tipo']=="1":
		FormaPago(nombre=request.POST['nombre']).save()
	elif request.POST['tipo']=="2":
		FormaFacturacion(nombre=request.POST['nombre']).save()
	elif request.POST['tipo']=="3":
		TipoAlquiler(nombre=request.POST['nombre']).save()

	return HttpResponse(json.dumps({}), content_type='application/json')

def EliminarCatalogo(request):
	if request.POST['tipo']=="1":
		FormaPago.objects.filter(forma_pago_id=request.POST['id']).delete()
	elif request.POST['tipo']=="2":
		FormaFacturacion.objects.filter(forma_facturacion_id=request.POST['id']).delete()
	elif request.POST['tipo']=="3":
		TipoAlquiler.objects.filter(tipo_alquiler_id=request.POST['id']).delete()

	return HttpResponse(json.dumps({}), content_type='application/json')

def GuardarCambiosCatalogo(request):
	if request.POST['tipo']=="1":
		FormaPago.objects.filter(forma_pago_id=request.POST['id']).update(nombre=request.POST['nombre'])
	elif request.POST['tipo']=="2":
		FormaFacturacion.objects.filter(forma_facturacion_id=request.POST['id']).update(nombre=request.POST['nombre'])
	elif request.POST['tipo']=="3":
		TipoAlquiler.objects.filter(tipo_alquiler_id=request.POST['id']).update(nombre=request.POST['nombre'])

	return HttpResponse(json.dumps({}), content_type='application/json')

def ReservasView(request):
	data = []
	for complejo in Complejo.objects.all():
		data.append({'id':complejo.complejo_id,'nombre':complejo.nombre})
	return render(request,'reservas.html',{'data':data})

def dt_eventos(request):
	str_query = """SELECT 
						 r.reserva_id
						,r.nombre_evento
						,CASE
							WHEN c.cliente_id IS NOT NULL THEN c.nombre
							ELSE e.nombre
						 END cliente
						,CASE
							WHEN c.cliente_id IS NOT NULL THEN c.telefono
							ELSE e.telefono_contacto
						 END telefono
						,CASE
							WHEN c.cliente_id IS NOT NULL THEN c.correo
							ELSE e.correo_contacto
						 END correo
						,u.usuario
					FROM
						modulo_1_reserva r
						JOIN modulo_1_usuario u ON u.usuario_id = r.usuario_id
						LEFT JOIN modulo_1_cliente c ON c.cliente_id = r.cliente_id
						LEFT JOIN modulo_1_empresa e ON e.empresa_id = r.empresa_id"""
	cursor = connection.cursor()
	cursor.execute(str_query)
	qs = cursor.fetchall()
	tipo_alquiler = convert_fetchall(qs)
	return HttpResponse(json.dumps(tipo_alquiler), content_type='application/json')

def CargarCombos(request):
	formas_pago = FormaPago.objects.all()
	formas_facturacion = FormaFacturacion.objects.all()
	tipos_alquiler = TipoAlquiler.objects.all()
	str_forma_pago = ""
	str_forma_facturacion = ""
	str_tipo_alquiler = ""

	for forma_pago in formas_pago:
		str_forma_pago += "<option value='"+str(forma_pago.forma_pago_id)+"'>"+forma_pago.nombre+"</option>"
	for forma_facturacion in formas_facturacion:
		str_forma_facturacion += "<option value='"+str(forma_facturacion.forma_facturacion_id)+"'>"+forma_facturacion.nombre+"</option>"
	for tipo_alquiler in tipos_alquiler:
		str_tipo_alquiler += "<option value='"+str(tipo_alquiler.tipo_alquiler_id)+"'>"+tipo_alquiler.nombre+"</option>"
	#for tipo_alquiler in tipos_alquiler:
	#	if request.session['type_user'] == 'B' and (tipo_alquiler.tipo_alquiler_id == 3 or tipo_alquiler.tipo_alquiler_id == 4):
	#		str_tipo_alquiler += "<option value='"+str(tipo_alquiler.tipo_alquiler_id)+"'>"+tipo_alquiler.nombre+"</option>"
	#	elif request.session['type_user'] == 'R' or request.session['type_user'] == 'A':
	#		str_tipo_alquiler += "<option value='"+str(tipo_alquiler.tipo_alquiler_id)+"'>"+tipo_alquiler.nombre+"</option>"

	data={
		'forma_pago': str_forma_pago,
		'forma_facturacion': str_forma_facturacion,
		'tipo_alquiler': str_tipo_alquiler,
	}

	return HttpResponse(json.dumps(data), content_type='application/json')

def InformacionEvento(request):
	reserva = Reserva.objects.get(reserva_id = request.POST['id_evento'])
	cliente = ""
	cliente_id = ""
	if reserva.cliente_id != None:
		cliente = reserva.cliente.nombre
		cliente_id = reserva.cliente.cliente_id
	else:
		cliente = reserva.empresa.nombre
		cliente_id = reserva.empresa.empresa_id

	evento = {
			'reserva':reserva.reserva_id,
			'nombre':reserva.nombre_evento,
			'estado':reserva.estado,
			'precio':str(reserva.precio),
			'costo':str(reserva.costo),
			'saldo':str(reserva.saldo),
			'notas':reserva.notas,
			'facturacion':reserva.forma_facturacion_id,
			'pago':reserva.forma_pago_id,
			'alquiler':reserva.tipo_alquiler_id,
			'cliente':cliente,
			'cliente_id':cliente_id
			}

	return HttpResponse(json.dumps(evento), content_type='application/json')

def ClientesAutocomplete(request):
	clientes = Cliente.objects.filter(nombre__icontains=request.GET['term'])
	empresas = Empresa.objects.filter(nombre__icontains=request.GET['term'])
	results = []
	for cliente in clientes:
		cliente_json = {}
		cliente_json['id'] = cliente.cliente_id
		cliente_json['label'] = cliente.nombre
		results.append(cliente_json)
	for empresa in empresas:
		empresa_json = {}
		empresa_json['id'] = empresa.empresa_id
		empresa_json['label'] = empresa.nombre
		results.append(empresa_json)

	data = json.dumps(results)
	return HttpResponse(data, content_type='application/json')

def GuardarEvento(request):
	usuario = Usuario.objects.filter(usuario=request.session['user_log'])
	cliente = Cliente.objects.filter(cliente_id=request.POST['cliente_id'],nombre=request.POST['nombre_cliente'])
	empresa = Empresa.objects.filter(empresa_id=request.POST['cliente_id'],nombre=request.POST['nombre_cliente'])
	if request.session['type_user'] == 'B' and (request.POST['reserva'] != "3" and request.POST['reserva'] != "4"):
		respuesta = {
					'error': True,
					'mensaje':"<li><b>Tipo de reserva:</b> No posee permisos para realizar este tipo de reserva (sólo prestamos o PEF).</li>"
		}
		return HttpResponse(json.dumps(respuesta), content_type='application/json')

	if len(cliente)>0:
		reserva = Reserva(nombre_evento=request.POST['nombre'],cliente_id=request.POST['cliente_id'],tipo_alquiler_id=request.POST['reserva'],
					forma_pago_id=request.POST['pago'],forma_facturacion_id=request.POST['facturacion'],estado=request.POST['estado'],
					notas=request.POST['notas'],usuario=usuario[0]).save()
		respuesta ={'error':False,'mensaje':"<li>Evento ingresado con éxito </li>",'id_evento':Reserva.objects.latest('reserva_id').reserva_id}
	elif len(empresa)>0:
		reserva = Reserva(nombre_evento=request.POST['nombre'],empresa_id=request.POST['cliente_id'],tipo_alquiler_id=request.POST['reserva'],
					forma_pago_id=request.POST['pago'],forma_facturacion_id=request.POST['facturacion'],estado=request.POST['estado'],
					notas=request.POST['notas'],usuario=usuario[0]).save()
		respuesta ={'error':False,'mensaje':"<li>Evento ingresado con éxito </li>",'id_evento':Reserva.objects.latest('reserva_id').reserva_id}
	else:
		respuesta = {
					'error': True,
					'mensaje':"<li><b>Cliente:</b> El cliente o la empresa no se encuentra registrado</li>"
		}

	return HttpResponse(json.dumps(respuesta), content_type='application/json')

def GuardarCambiosEvento(request):
	cliente = Cliente.objects.filter(cliente_id=request.POST['cliente_id'],nombre=request.POST['nombre_cliente'])
	empresa = Empresa.objects.filter(empresa_id=request.POST['cliente_id'],nombre=request.POST['nombre_cliente'])
	respuesta = {'error':False,'mensaje':"<li>Evento actualizado con éxito </li>"}
	
	if request.session['type_user'] == 'B' and (request.POST['reserva'] != "3" and request.POST['reserva'] != "4"):
		respuesta = {
					'error': True,
					'mensaje':"<li><b>Tipo de reserva:</b> No posee permisos para realizar este tipo de reserva (sólo prestamos o PEF).</li>"
		}
		return HttpResponse(json.dumps(respuesta), content_type='application/json')

	if len(cliente)>0:
		reserva = Reserva.objects.filter(reserva_id=request.POST['id_evento']).update(nombre_evento=request.POST['nombre'],cliente_id=request.POST['cliente_id'],tipo_alquiler_id=request.POST['reserva'],
					forma_pago_id=request.POST['pago'],forma_facturacion_id=request.POST['facturacion'],estado=request.POST['estado'],
					notas=request.POST['notas'])
	elif len(empresa)>0:
		reserva = Reserva.objects.filter(reserva_id=request.POST['id_evento']).update(nombre_evento=request.POST['nombre'],empresa_id=request.POST['cliente_id'],tipo_alquiler_id=request.POST['reserva'],
					forma_pago_id=request.POST['pago'],forma_facturacion_id=request.POST['facturacion'],estado=request.POST['estado'],
					notas=request.POST['notas'])
	else:
		respuesta = {
					'error': True,
					'mensaje':"<li><b>Cliente:</b> El cliente o la empresa no se encuentra registrado</li>"
		}

	return HttpResponse(json.dumps(respuesta), content_type='application/json')

def CargarCanchas(request):
	str_cancha="<option value=\"-1\">Seleccione la cancha</option>"
	for cancha in Cancha.objects.filter(complejo_id=request.POST['id']):
		str_cancha += "<option value=\""+str(cancha.cancha_id)+"\">"+cancha.nombre+"</option>"
	return HttpResponse(json.dumps({'str_cancha':str_cancha}), content_type='application/json')

def dt_reservas(request):
	str_query = """SELECT 
						 rc.reserva_cancha_id
						,co.complejo_id
						,ca.cancha_id
						,co.nombre
						,ca.nombre
						,rc.fecha::text AS fecha
						,rc.hora_inicio::text AS inicio
						,rc.hora_fin::text AS fin
						,'$'::text || rc.precio_sugerido::text AS precio_sugerido
					FROM
						modulo_1_reserva r
						JOIN modulo_1_reservacancha rc ON rc.reserva_id = r.reserva_id
						JOIN modulo_1_cancha ca ON ca.cancha_id = rc.cancha_id
						JOIN modulo_1_complejo co ON co.complejo_id = ca.complejo_id
					WHERE r.reserva_id = """+request.POST['evento']
	cursor = connection.cursor()
	cursor.execute(str_query)
	qs = cursor.fetchall()
	tipo_alquiler = convert_fetchall(qs)
	return HttpResponse(json.dumps(tipo_alquiler), content_type='application/json')

def GuardarPrecio(request):
	Reserva.objects.filter(reserva_id=request.POST['id_evento']).update(precio=request.POST['precio_evento'],costo=request.POST['costo_evento'])
	return HttpResponse(json.dumps({}), content_type='application/json')

def GuardarReserva(request):
	usuario = Usuario.objects.filter(usuario=request.session['user_log'])
	ReservaCancha(cancha_id=request.POST['cancha'],reserva_id=request.POST['evento'],usuario=usuario[0],fecha=request.POST['fecha'],
				hora_inicio=request.POST['inicio'],hora_fin=request.POST['fin'],notas=request.POST['notas'],
				precio_sugerido=request.POST['precio_sugerido']).save()
	return HttpResponse(json.dumps({'error':False}), content_type='application/json')

def InformacionReserva(request):
	reserva = ReservaCancha.objects.get(reserva_cancha_id = request.POST['id_reserva'])

	reserva_cancha = {
			'complejo':reserva.cancha.complejo_id,
			'cancha':reserva.cancha.cancha_id,
			'fecha':str(reserva.fecha),
			'inicio':str(reserva.hora_inicio),
			'fin':str(reserva.hora_fin),
			'precio_sugerido':str(reserva.precio_sugerido),
			'notas':reserva.notas,
			}

	return HttpResponse(json.dumps(reserva_cancha), content_type='application/json')