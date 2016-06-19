from django.shortcuts import render

def login(request):
	return render(request,'login.html')

def home(request):
	return render(request,'index.html')

def change_pass(request):
	return render(request,'cambiar_password.html')