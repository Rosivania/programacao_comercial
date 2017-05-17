from django.shortcuts import render
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView, DetailView
from solicitacao.models import Solicitacao
from solicitacao.forms import *
from livros.models import *
from livros.forms import *
from django.db.models import Q
from django.core.urlresolvers import reverse_lazy


# class SolicitacaoNew(CreateView):
#     """
#     View para cadastro de novos livros
#     """
#     model = Solicitacao 
#     form_class = FormularioSolicitacao
#     template_name = 'solicitacao/Novo.html'
#     success_url = reverse_lazy('livros:listar-meus')

#     def form_valid(self, form):
#         form.instance.usuario_solicitante = self.request.user
#         form.instance.usuario_solicitado = self.request.user.livros
#         return super(SolicitacaoNew, self).form_valid(form)

class SolicitacaoNew(CreateView):
	model = Solicitacao
	form_class = FormularioSolicitacao
	template_name = 'solicitacao/Novo.html'
	success_url = reverse_lazy('livros:listar')
	def form_valid(self, form):
		livro_id = self.request.GET.get('livro', '')
		livro = Livro.objects.get(id=livro_id)
		form.instance.usuario_solicitante = self.request.user
		form.instance.usuario_solicitado = livro.usuario
		livro.disponivel = 'False'
		livro.save()
		return super(SolicitacaoNew, self).form_valid(form)

		
	#def get(self, request):

	# 	livro_id = self.request.GET.get('livro', '')

	# 	livro = Livro.objects.get(id=livro_id)
	# 	usuario_solicitante_id = self.request.GET.get('usuario_solicitante_id','')
 #        usuario = User.objects.get(id=usuario_solicitante_id)
	# 	livro_solicitado = livro
	# 	usuario_solicitado = livro.usuario
	# 	usuario_solicitante = usuario
	# 	livro_solicitado.save()
	# 	usuario_solicitado_id.save()
	# 	usuario_solicitante_id.save()

	# 	# solicitacao = Solicitacao(
	# 	# 	livro_solicitado=livro,
	# 	# 	usuario_solicitante_id=self.request.user,
	# 	# 	usuario_solicitado_id=livro.usuario,
	# 	# )
	# 	# solicitacao.save()

	# 	context = {
	# 		'livro_solicitado': livro_solicitado,
	# 		'usuario_solicitado_id': usuario_solicitado_id,
	# 		'usuario_solicitante_id': usuario_solicitante_id,
	# 	}
	# 	return render(request, 'solicitacao/solicitar.html',context)
