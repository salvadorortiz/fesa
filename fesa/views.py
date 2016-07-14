from django.shortcuts import render

def login(request):
	try:
		del request.session['user_log']
		del request.session['type_user']
	except KeyError:
		pass
	return render(request,'login.html')

def home(request):
	if not request.session.has_key('user_log'):
		return render(request,'login.html')
	return render(request,'reservas.html')

def change_pass(request):
	if not request.session.has_key('user_log'):
		return render(request,'login.html')
	return render(request,'cambiar_password.html')