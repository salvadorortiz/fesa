#-*- coding: utf-8 -*-
from django.db import models
from django.core.validators  import validate_email, RegexValidator

phone_regex = RegexValidator(regex=r'^([(][0-9]+[)]) ([0-9-][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9])$' , message= "El teléfono no cumple con un formato válido")

class Usuario(models.Model):
	TIPO = 	(
			('A','Tipo A'),
			('B','Tipo B'),
			('R','Administrador')
			)
	usuario_id = models.AutoField(primary_key=True)
	nombre = models.CharField('Nombre',max_length=100,blank=False,null=False,default='')
	area = models.CharField('Área',max_length=50,blank=False,null=False)
	jefe_directo = models.CharField('Jefe Directo',max_length=100,blank=False,null=False,default='')
	estado = models.BooleanField('Estado', default=True)
	tipo_usuario =  models.CharField('Tipo Usuario',max_length=1,choices=TIPO,null=False,blank=False,default='')
	usuario = models.CharField('Usuario',max_length=50,blank=False,null=False,default='')
	password = models.CharField('Contraseña',max_length=100,blank=False,null=False,default='')
	
	def __unicode__(self):
		return self.nombre

class Complejo(models.Model):
	complejo_id = models.AutoField(primary_key=True)
	direccion = models.TextField('Dirección', max_length=250, blank=True, null=True)
	nombre = models.CharField('Nombre',max_length=100,blank=False,null=False,default='')

	def __unicode__(self):
		return self.nombre

"""class HorarioComplejo(models.Model):
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
	hora_cierre = models.TimeField(auto_now=False,auto_now_add=False)"""

class Cancha(models.Model):
	cancha_id = models.AutoField(primary_key=True)
	nombre = models.CharField('Nombre',max_length=100,blank=False,null=False,default='')
	complejo = models.ForeignKey('Complejo',verbose_name='Complejo',null=False,blank=False)
	horas_posibles = models.IntegerField('Horas posibles', blank=False, default=0)

	def __unicode__(self):
		return self.nombre

class PrecioXCancha(models.Model):
	DIAS = 	(
			('X','Lunes-Viernes'),
			('S','Sábado'),
			('D','Domingo'),
			)
	precio_cancha_id = models.AutoField(primary_key=True)
	cancha = models.ForeignKey('Cancha',verbose_name='Cancha',null=False,blank=False)
	precio = models.DecimalField('Precio',max_digits=10, decimal_places=2, blank=False, default=0.0)
	dia = models.CharField('Dia',max_length=1,choices=DIAS,null=False,blank=False,default='')
	hora_apertura = models.TimeField(auto_now=False,auto_now_add=False)
	hora_cierre = models.TimeField(auto_now=False,auto_now_add=False)

class Cliente(models.Model):
	cliente_id = models.AutoField(primary_key=True)
	codigo = models.CharField('Código',max_length=20,blank=True,null=True,default='')
	nombre = models.CharField('Nombre',max_length=100,blank=False,null=False,default='')
	DUI = models.CharField('DUI',max_length=10,blank=True,null=True,default='')
	telefono = models.CharField('Teléfono', max_length=15, validators=[phone_regex], blank=False, null=False)
	telefono_alterno = models.CharField('Teléfono alterno', max_length=15, validators=[phone_regex], blank=True,null=True)
	correo = models.EmailField('Correo electrónico', max_length=60, blank=True, validators=[validate_email],null=True)
	direccion = models.TextField('Dirección', max_length=250, blank=True, null=True)
	ingresado_por= models.CharField('IngresadoPor',max_length=20,blank=True,null=True,default='')
	
	def __unicode__(self):
		return self.nombre

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
	ingresado_por= models.CharField('IngresadoPor',max_length=20,blank=True,null=True,default='')

	def __unicode__(self):
		return self.nombre

class FormaPago(models.Model):
	forma_pago_id = models.AutoField(primary_key=True)
	nombre = models.CharField('Nombre',max_length=100,blank=False,null=False,default='')

	def __unicode__(self):
		return self.nombre

class FormaFacturacion(models.Model):
	forma_facturacion_id = models.AutoField(primary_key=True)
	nombre = models.CharField('Nombre',max_length=100,blank=False,null=False,default='')

	def __unicode__(self):
		return self.nombre

class TipoAlquiler(models.Model):
	tipo_alquiler_id = models.AutoField(primary_key=True)
	nombre = models.CharField('Nombre',max_length=100,blank=False,null=False,default='')

	def __unicode__(self):
		return self.nombre

class Reserva(models.Model):
	ESTADO = 	(
				('C','Confirmado'),
				('T','Tentativo'),
				('R','Realizado'),
				('N','No realizado')
				)
	reserva_id = models.AutoField(primary_key=True)
	nombre_evento = models.CharField('Nombre del evento',max_length=100,blank=False,null=False,default='')
	cliente = models.ForeignKey('Cliente',verbose_name='Cliente',null=True,blank=True) 
	empresa = models.ForeignKey('Empresa',verbose_name='Empresa',null=True,blank=True)
	usuario = models.ForeignKey('Usuario',verbose_name='Usuario')
	tipo_alquiler = models.ForeignKey('TipoAlquiler',verbose_name='Tipo de alquiler',null=False,blank=False)
	forma_pago = models.ForeignKey('FormaPago',verbose_name='Forma de pago',null=False,blank=False)
	forma_facturacion = models.ForeignKey('FormaFacturacion',verbose_name='Forma de facturación',null=False,blank=False)
	estado = models.CharField('Dias',max_length=1,choices=ESTADO,null=False,blank=False,default='')
	precio = models.DecimalField('Precio',max_digits=10, decimal_places=2, blank=True, null=True)
	costo = models.DecimalField('Costo',max_digits=10, decimal_places=2, blank=True, null=True)
	saldo = models.DecimalField('Saldo',max_digits=10, decimal_places=2, blank=False, default=0.0)
	fecha_ingreso = models.DateField('Fecha de ingreso',auto_now_add=True)
	notas = models.TextField('Área',max_length=500,blank=True,null=True)

	def __unicode__(self):
		return self.nombre_evento

class ReservaCancha(models.Model):
	reserva_cancha_id = models.AutoField(primary_key=True)
	cancha = models.ForeignKey('Cancha',verbose_name='Cancha',null=False,blank=False)
	reserva = models.ForeignKey('Reserva',verbose_name='Reserva',null=False,blank=False)
	usuario = models.ForeignKey('Usuario',verbose_name='Usuario')
	fecha = models.DateField(auto_now=False,auto_now_add=False)
	hora_inicio = models.TimeField(auto_now=False,auto_now_add=False)
	hora_fin = models.TimeField(auto_now=False,auto_now_add=False)
	precio_sugerido = models.DecimalField('Precio Sugerido',max_digits=10, decimal_places=2, blank=False, default=0.0)
	notas = models.TextField('Área',max_length=500,blank=True,null=True)

class RemesaXReserva(models.Model):
	remesa_reserva_id = models.AutoField(primary_key=True)
	reserva = models.ForeignKey('Reserva',verbose_name='Reserva',null=False,blank=False)
	usuario = models.ForeignKey('Usuario',verbose_name='Usuario')
	numero_remesa = models.CharField('Número de remesa',max_length=100,blank=False,null=False,default='')
	monto = models.DecimalField('Monto',max_digits=10, decimal_places=2, blank=False, default=0.0)
	fecha_ingreso = models.DateField('Fecha de ingreso',auto_now_add=True)
	fecha = models.DateField(auto_now=False,auto_now_add=False)