#-*- coding: utf-8 -*-
from django.db import models
from django.core.validators  import validate_email, RegexValidator

phone_regex = RegexValidator(regex=r'^(([(][0-9]+[)])( |[0-9-]+)+([ ](ext|EXT)[ ][0-9]+)(,|-)?)+$' , message= "El teléfono no cumple con un formato válido: (503) 2256 45 54 EXT 123 ó (503) 2256-4554 EXT 123")

class Usuario(models.Model):
	TIPO = 	(
			('A','Tipo A'),
			('B','Tipo B'),
			('R','Administrador')
			)
	usuario_id = models.AutoField(primary_key=True)
	nombre = models.CharField('Nombre',max_length=100,blank=False,null=False,default='')
	area = models.TextField('Área',max_length=50,blank=False,null=False)
	jefe_directo = models.CharField('Jefe Directo',max_length=100,blank=False,null=False,default='')
	estado = models.BooleanField('Estado', default=True)
	tipo_usuario =  models.CharField('Tipo Usuario',max_length=1,choices=TIPO,null=False,blank=False,default='')
	user = models.CharField('Nombre',max_length=50,blank=False,null=False,default='')
	password = models.CharField('Contraseña',max_length=50,blank=False,null=False,default='123')
	
	def __str__(self):
		return self.nombre

class Complejo(models.Model):
	complejo_id = models.AutoField(primary_key=True)
	nombre = models.CharField('Nombre',max_length=100,blank=False,null=False,default='')

	def __str__(self):
		return self.nombre

class HorarioComplejo(models.Model):
	DIAS = 	(
			('L','Lunes'),
			('M','Martes'),
			('X','Miércoles'),
			('J','Jueves'),
			('V','Viernes'),
			('S','Sábado'),
			('D','Domingo'),
			)
	horario_complejo_id = models.AutoField(primary_key=True)
	complejo = models.ForeignKey('Complejo', related_name='complejo', verbose_name='Complejo')
	dia = models.CharField('Dias',max_length=1,choices=DIAS,null=False,blank=False,default='')
	hora_apertura = models.TimeField(auto_now=False,auto_now_add=False)
	hora_cierre = models.TimeField(auto_now=False,auto_now_add=False)

class Cancha(models.Model):
	cancha_id = models.AutoField(primary_key=True)
	nombre = models.CharField('Nombre',max_length=100,blank=False,null=False,default='')
	complejo = models.ForeignKey('Complejo',verbose_name='Complejo',null=False,blank=False)
	precio = models.DecimalField('Precio',max_digits=10, decimal_places=2, blank=False, default=0.0)
	horas_posibles = models.IntegerField('Horas posibles', blank=True, default=0)

	def __str__(self):
		return self.nombre

class Cliente(models.Model):
	cliente_id = models.AutoField(primary_key=True)
	codigo = models.CharField('Código',max_length=20,blank=True,null=True,default='')
	nombre = models.CharField('Nombre',max_length=100,blank=False,null=False,default='')
	DUI = models.CharField('DUI',max_length=10,blank=True,null=True,default='')
	telefono = models.CharField('Teléfono', max_length=50, validators=[phone_regex], blank=False)
	telefono_alterno = models.CharField('Teléfono alterno', max_length=50, validators=[phone_regex], blank=True)
	correo = models.EmailField('Correo electrónico', max_length=60, blank=True, validators=[validate_email])
	direccion = models.TextField('Dirección', max_length=250, blank=True)

class Empresa(models.Model):
	empresa_id = models.AutoField(primary_key=True)
	codigo = models.CharField('Código',max_length=20,blank=True,null=True,default='')
	nombre = models.CharField('Nombre',max_length=100,blank=False,null=False,default='')
	nit = models.CharField('Nombre',max_length=17,blank=False,null=False,default='')
	registro_iva = models.CharField('Registro',max_length=50,blank=False,null=False,default='')
	telefono = models.CharField('Teléfono', max_length=50, validators=[phone_regex], blank=False, null=False)
	contacto = models.CharField('Persona de contacto',max_length=100,blank=False,null=False,default='')
	telefono_contacto = models.CharField('Teléfono de contacto', max_length=50, validators=[phone_regex], blank=False, null=False)
	correo_contacto = models.EmailField('Correo electrónico de contacto', max_length=60, blank=True, validators=[validate_email])

class FormaPago(models.Model):
	forma_pago_id = models.AutoField(primary_key=True)
	nombre = models.CharField('Nombre',max_length=100,blank=False,null=False,default='')

class FormaFacturacion(models.Model):
	forma_facturacion_id = models.AutoField(primary_key=True)
	nombre = models.CharField('Nombre',max_length=100,blank=False,null=False,default='')

class TipoAlquiler(models.Model):
	tipo_alquiler_id = models.AutoField(primary_key=True)
	nombre = models.CharField('Nombre',max_length=100,blank=False,null=False,default='')

class Reserva(models.Model):
	ESTADO = 	(
				('C','Confirmado'),
				('T','Tentativo'),
				)
	reserva_id = models.AutoField(primary_key=True)
	nombre_evento = models.CharField('Nombre del evento',max_length=100,blank=False,null=False,default='')
	cliente = models.ForeignKey('Cliente',verbose_name='Cliente',null=True,blank=True) 
	empresa = models.ForeignKey('Empresa',verbose_name='Empresa',null=True,blank=True)
	tipo_alquiler = models.ForeignKey('TipoAlquiler',verbose_name='Tipo de alquiler',null=False,blank=False)
	forma_pago = models.ForeignKey('FormaPago',verbose_name='Forma de pago',null=False,blank=False)
	forma_facturacion = models.ForeignKey('FormaFacturacion',verbose_name='Forma de facturación',null=False,blank=False)
	estado = models.CharField('Dias',max_length=1,choices=ESTADO,null=False,blank=False,default='')
	precio = models.DecimalField('Precio',max_digits=10, decimal_places=2, blank=False, default=0.0)
	costo = models.DecimalField('Costo',max_digits=10, decimal_places=2, blank=False, default=0.0)
	remesado = models.DecimalField('Remesado',max_digits=10, decimal_places=2, blank=False, default=0.0)
	remanente = models.DecimalField('Remanente',max_digits=10, decimal_places=2, blank=False, default=0.0)
	notas = models.TextField('Área',max_length=500,blank=True,null=True)

class ReservaCancha(models.Model):
	reserva_cancha_id = models.AutoField(primary_key=True)
	cancha = models.ForeignKey('Cancha',verbose_name='Cancha',null=False,blank=False)
	reserva = models.ForeignKey('Reserva',verbose_name='Reserva',null=False,blank=False)
	fecha = models.DateField(auto_now=False,auto_now_add=False)
	hora = models.TimeField(auto_now=False,auto_now_add=False)
	notas = models.TextField('Área',max_length=500,blank=True,null=True)