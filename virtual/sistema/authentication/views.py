# -*- coding: utf-8 -*-
from django.views.generic import View
from django.shortcuts import render

class Autenticacao(View):
	"""
	View
	"""
	def get(self, request):
		context = {	}
		return render(request, 'authentication/login.html', context)
