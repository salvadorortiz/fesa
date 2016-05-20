# -*- coding: utf-8 -*-

from modulo_1.models import *
from django import forms
from django.forms.fields import CharField
from django.forms import ModelForm,Textarea

class ClienteForm(ModelForm):
	#your_name = forms.CharField(label='Your name', max_length=100)

	class Meta:
		model = Cliente
		fields = ['codigo', 'nombre', 'DUI', 'telefono','telefono_alterno','correo','direccion']
		

class EmpresaForm(ModelForm):

	class Meta:
		model= Empresa
		fields= ['codigo','nombre','nit','registro_iva','telefono','contacto','telefono_contacto','correo_contacto']

	def __init__(self,*args,**kwargs):
		super(EmpresaForm,self).__init__(*args,**kwargs)
		self.fields['codigo'].empty_label= 'Código'