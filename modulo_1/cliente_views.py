from django.shortcuts import render
from modulo_1.forms import ClienteForm

def RegistroClienteView(request):
	data={'usuario': 'Kate', 'cliente_form': ClienteForm()}
	return render(request,'registrocliente.html',data)