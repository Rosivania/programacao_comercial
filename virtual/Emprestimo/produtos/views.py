from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from produtos.forms import *
from produtos.models import *


class ProdutosNew(CreateView):
    """
    View para criação de novos produtos
    """
    model = Produto
    form_class = FormularioProduto
    template_name = 'produtos/NovoProduto.html'
    success_url = reverse_lazy('listar-produtos')


class ProdutosEdit(UpdateView):
    """
    View para a edição de produtos já cadastrados.
    """
    model = Produto
    form_class = FormularioProduto
    template_name = 'produtos/EditarProduto.html'
    success_url = reverse_lazy('editar-produto')


class ProdutosDelete(DeleteView):
    """
    View para a exclusão de produtos.
    """
    model = Produto
    template_name = 'produtos/ExcluirProduto.html'
    success_url = reverse_lazy('listar-produtos')

class ProdutosList(ListView):
    """
    View para listar os Produtos
    """
    model = Produto
    template_name = 'produtos/listarProdutos.html'



class ProdutosListarCategoria(ListView):
    """
    View para listar os Produtos cadastrados por categoria
    """
    model = Produto
    template_name = 'produtos/listarProdutos.html'

    def get_queryset(self):
        queryset = Produto.objects.filter(categoria=self.kwargs['categoria'])
        return queryset
