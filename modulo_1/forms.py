# -*- coding: utf-8 -*-

from modulo_1.models import *
from django import forms
from django.forms.fields import CharField
from django.forms import ModelForm,Textarea,MultipleChoiceField,HiddenInput
                                             

class ClienteForm(ModelForm):
	#your_name = forms.CharField(label='Your name', max_length=100)

	class Meta:
		model = Cliente
		fields = ['codigo', 'nombre', 'DUI','ingresado_por', 'telefono','telefono_alterno','correo','direccion']	
		widgets={
			'ingresado_por' : HiddenInput(),
		}

class EmpresaForm(ModelForm):

	class Meta:
		model= Empresa
		fields= ['codigo','nombre','nit','ingresado_por','registro_iva','telefono','contacto','telefono_contacto','correo_contacto']
		widgets={
			'ingresado_por' : HiddenInput(),
		}
		
	def __init__(self,*args,**kwargs):
		super(EmpresaForm,self).__init__(*args,**kwargs)
		self.fields['codigo'].empty_label= 'Código'

class UsuarioForm(ModelForm):

	class Meta:
		model = Usuario
		fields = ['nombre', 'area', 'jefe_directo', 'estado','tipo_usuario','usuario','password']
		
	def __init__(self, *args, **kwargs):
		super(UsuarioForm, self ).__init__(*args, **kwargs)
		self.fields['tipo_usuario'].empty_label = "Seleccione el tipo de usuario"
		
class ComplejoForm(ModelForm):
	class Meta:
		model= Complejo
		fields= ['nombre','direccion']

class HorarioCanchaForm(ModelForm):
	DIAS = 	(
			('X','Lunes-Viernes'),
			('S','Sábado'),
			('D','Domingo'),
			)
	#your_name = forms.CharField(label='Your name', max_length=100)
	dia = forms.MultipleChoiceField(choices=DIAS, required=True, widget=forms.CheckboxSelectMultiple())
	class Meta:
		model= PrecioXCancha
		fields = ['cancha','dia','hora_apertura','hora_cierre']
		widgets={
			'dia' : HiddenInput(),
		}

class CanchaForm(ModelForm):
	class Meta:
		model= Cancha
		fields= ['nombre','complejo','horas_posibles']
		widgets={
			'complejo': HiddenInput(),
		}