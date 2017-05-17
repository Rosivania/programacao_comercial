# -*- coding: utf-8 -*-
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
#from django.contrib.auth.mixins import LoginRequiredMixin
#from django.contrib.auth.models import User


class Autenticacao(View):
	"""
	View - Autenticação de usuários
	"""
	def get(self, request):
		context={}
		if self.request.user.is_authenticated():
			return redirect('/livros')
			#return render(request, 'index.html',context )
			#return redirect(reverse_lazy('livros:listar'))
		return render(request, 'autenticacao/login.html', context)

	def post(self, request):
		context = {}
		usuario = request.POST.get("username")
		senha = request.POST.get("password")
		user = authenticate(username=usuario, password=senha)
		if user is not None:
		    login(self.request, user)
		    return redirect('/livros')
		    #return render(request, 'index.html', context)
		else:
		    context.update(message='Login ou Senha incorreto(s)')

		return render(request, 'autenticacao/login.html', context)


class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('/')
