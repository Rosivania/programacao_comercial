from django.shortcuts import render
from django.views.generic import View, ListView, CreateView
from django.views.generic.edit import DeleteView, UpdateView
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.urls import reverse_lazy 
from livros.forms import *
from livros.models import *




class LivrosNew(CreateView):
    """
    View para cadastro de novos livros
    """
    model = Livro 
    form_class = FormularioLivro
    template_name = 'livros/Novo.html'
    success_url = reverse_lazy('livros:listar-meus')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(LivrosNew, self).form_valid(form)


class LivrosEdit(UpdateView):
    """
    View para a edição de livros já cadastrados.
    """
    model = Livro 
    form_class = FormularioLivro
    template_name = 'livros/Editar.html'
    success_url = reverse_lazy('livros:listar-meus')


class LivrosDelete(DeleteView):
    """
    View para a exclusão de livros.
    """
    model = Livro 
    #template_name = 'livros/Excluir.html'
    success_url = reverse_lazy('livros:listar-meus')

class LivrosList(ListView):
    """
    View para listar os Livros
    """
    model = Livro 
    template_name = 'index.html'
    def get_queryset(self):
        return Livro.objects.exclude(usuario = self.request.user).order_by('titulo')
        #return Livro.objects.order_by('titulo')

class LivrosListar(ListView):
    """
    View para listar os Livros do usuário
    """
    model = Livro 
    template_name = 'livros/Listar.html'
    def get_queryset(self):
        return Livro.objects.filter(usuario=self.request.user).order_by('titulo')

class MinhaListView(ListView):
    model = Livro
    template_name = 'index.html'
    context_object_name = 'resultados'

    def get_queryset(self, **kwargs):
        filtro1 = self.request.GET.get('parametro1', '')
        filtro2 = self.request.GET.get('parametro2', '')
        return Livro.objects.filter(Q(titulo__icontains=filtro1) | Q(editora__icontains=filtro2))

class LivrosBuscar(ListView):
    model = Livro
    template_name = 'index.html'
    def get_queryset(self, **kwargs):
        filtro = self.request.GET.get('filtro', '')
        print(filtro)
        return Livro.objects.exclude(usuario = self.request.user).filter(
            Q(titulo__icontains=filtro)|
            Q(categoria__icontains=filtro)|
            Q(editora__icontains=filtro)
            ).order_by('titulo')

class LivrosListarCategoria(ListView):
    """
    View para listar os Livros cadastrados por categoria
    """
    model = Livro
    template_name = 'livros/Categoria.html'

    def get_queryset(self):

        print(self.request.GET.getlist('categoria'))
        #http://127.0.0.1:8000/livros/categoria/?categoria=1&categoria=9&categoria=12
        #categoria = self.request.GET.get('categoria')
        categorias = self.request.GET.getlist('categoria')
        return Livro.objects.exclude(usuario = self.request.user).filter(categoria__in=categorias).order_by('titulo')