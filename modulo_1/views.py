from django.shortcuts import render

def PreciosView(request):
	return render(request,'precios.html')