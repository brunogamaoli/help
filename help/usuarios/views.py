from django.shortcuts import render, redirect
from usuarios.forms import UserModelForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def cadastro(request): # Funcao para cadastrar um usuario
	form = UserModelForm(request.POST or None)
	context = {'form':form}
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('/cadastro')
	return render(request, 'usuarios/cadastro.html', context)

def do_login(request): # Funcao para realizar Login e redirecionar para a pagina inicial
	if request.method == "POST":
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			login(request, user)
			return redirect('base:home')
	return render(request, 'usuarios/login.html')

def do_logout(request): # Funcao para realizar Logout
	logout(request)
	return redirect('/login')

@login_required
def home(request): # Funcao para renderizar a pagina inicial
	return render(request, 'base/base.html')
