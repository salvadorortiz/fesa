from django.shortcuts import render

def home(request):
	data={'usuario': 'Kate'}
	return render(request,'index.html',data)