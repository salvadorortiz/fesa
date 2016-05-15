from django.shortcuts import render

def login(request):
	return render(request,'login.html')

def home(request):
	data={'usuario': 'Kate'}
	return render(request,'index.html',data)