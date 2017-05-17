from django.conf.urls import url
from livros import views
app_name = 'livros'
urlpatterns = [
	 url(r'^$', views.LivrosList.as_view(), name='listar'),
	 url(r'^lista_Pessoal/$', views.LivrosListar.as_view(), name='listar-meus'),
	 url(r'^categoria/$', views.LivrosListarCategoria.as_view(), name='categoria'),
	 url(r'^novo/$', views.LivrosNew.as_view(), name='novo'),
	 url(r'^buscar/$', views.LivrosBuscar.as_view(), name='buscar'),
	 url(r'^(?P<pk>\d+)/$', views.LivrosEdit.as_view(), name='editar'),
	 url(r'^deletar/(?P<pk>\d+)/$', views.LivrosDelete.as_view(), name='deletar'),
	 url(r'^disponivel/(?P<pk>\d+)/$', views.LivrosDisponivel.as_view(), name='disponivel'),
	 #url(r'^(?P<categoria>[\w-]+)$',views.ProdutosListarCategoria.as_view(), name = 'listar-produtos-categoria'),
]