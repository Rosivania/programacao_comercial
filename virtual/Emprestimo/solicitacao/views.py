from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView, DetailView
from solicitacao.models import Solicitacao
from solicitacao.forms import *
from livros.models import *
from livros.forms import *
from datetime import datetime
#from django.db.models import Q

class SolicitacaoNew(CreateView):
	"""
	View para solicitar emprestimos de livros.
	"""
	model = Solicitacao
	form_class = FormularioSolicitacao
	template_name = 'solicitacao/Novo.html'
	success_url = reverse_lazy('livros:listar')
	def form_valid(self, form):
		livro_id = self.request.GET.get('livro', '')
		livro = Livro.objects.get(id=livro_id)
		form.instance.usuario_solicitante = self.request.user
		form.instance.usuario_solicitado = livro.usuario
		#form.instance.livro_solicitado = livro_id
		livro.disponivel = 'False'
		livro.save()
		return super(SolicitacaoNew, self).form_valid(form)

class SolicitacaoList(ListView):
	"""
	View para listar emprestimos cadastrados/pendentes.
	"""
	model = Solicitacao
	template_name = 'solicitacao/Listar.html'
	def get_queryset(self):
		return Solicitacao.objects.filter(usuario_solicitante=self.request.user).exclude(devolvido='True')

class Devolucao(View):
	"""
	View para devolver livros solicitados. 
	"""
	def get(self, request):
		solicitacao_id = self.request.GET.get('solicitacao',0)
		solicitacao = Solicitacao.objects.get(id=solicitacao_id)
		solicitacao.devolvido = 'True'
		solicitacao.data_devolucao = datetime.now()
		solicitacao.save()
		return redirect(reverse_lazy('livros:listar'))


# class SolicitacaoListar(ListView):
#     """
#     View para listar os Livros 
#     """
#     model = Livro 
#     template_name = 'index.html'
#     def get_queryset(self):
#         return Solicitacao.objects.exclude(usuario_solicitante = self.request.user).filter(
#             devolvido ='True').order_by('titulo')

# class Devolver(UpdateView):
# 	"""
# 	View para editar solicitação de empréstimo de livros. 
# 	"""
# 	model = Solicitacao
# 	form_class = FormularioSolicitacao
# 	template_name = 'solicitacao/Editar.html'
# 	success_url = reverse_lazy('livros:listar')	
# 	def form_valid(self, form):
# 		livro_id = self.request.GET.get('livro', '')
# 		livro = Livro.objects.get(id=livro_id)
# 		form.instance.usuario_solicitante = self.request.user
# 		form.instance.usuario_solicitado = livro.usuario
# 		form.instance.devolvido = 'True'
# 		livro.disponivel = 'True'
# 		livro.save()
# 		return super(Devolver, self).form_valid(form)	

