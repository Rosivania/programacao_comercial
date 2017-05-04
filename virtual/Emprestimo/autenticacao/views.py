# -*- coding: utf-8 -*-
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.mixins import LoginRequiredMixin
#from django.contrib.auth.models import User
#from django.core.urlresolvers import reverse_lazy


class Autenticacao(View):
	"""
	View - Autenticação de usuários
	"""
	def get(self, request):
		context={}
		if self.request.user.is_authenticated():
			return render(request, 'index.html',context )
		return render(request, 'autenticacao/login.html', context)

	def post(self, request):
		context = {}
		usuario = request.POST.get("username")
		senha = request.POST.get("password")
		user = authenticate(username=usuario, password=senha)
		if user is not None:
		    login(self.request, user)
		    return render(request, 'index.html', context)
		else:
		    context.update(message='Login ou Senha incorreto(s)')
		    #resposta['mensagem'] = 'Login ou Senha incorreto(s)'

		return render(request, 'autenticacao/login.html', context)

# class Index(View):
# 	def get(self, request):
# 		return render('logado')
	
	# def login (self):
	# 	resposta ={
	# 	    'sucesso': False,
	# 	    'mensagem': ''
	# 	}
	# 	usuario = self.request.POST.get("login")
	# 	senha = self.request.POST.get("senha")
	# 	user = authenticate(username=usuario, password=senha)
	# 	if user:
	# 	    login(self.request, user)
	# 	    return redirect(self.request.POST.get('next', '/index'))
	# 	else:
	# 	    resposta['mensagem'] = 'Login ou Senha incorreto(s)'

	# 	return render(self.request, 'autenticacao/login.html', resposta)

# class Index(LoginRequiredMixin, View):
#     login_url = '/'

#     def get(self, request):

#         retorno = {
#             'nome' : 'Teste'
#         }
#         return render(request, 'index.html', retorno)

#     def post(self, request):
#         return render(request, 'index.html', {})


# class Logout(View):
#     def get(self,request):
#         logout(request)
#         return redirect('autenticacao')

#Logout:
def logout(request):
	logout(request)
	return redirect('/')

