from django.conf.urls import url
from livros import views
app_name = 'livros'
urlpatterns = [
	 url(r'^$', views.LivrosList.as_view(), name='listar'),
	 url(r'^categoria/$', views.LivrosListarCategoria.as_view(), name='categoria'),
	 url(r'^novo/$', views.LivrosNew.as_view(), name='novo'),
	 url(r'^(?P<pk>[0-9]+)/$', views.LivrosEdit.as_view(), name='editar'),
	 url(r'^excluir/(?P<pk>[0-9]+)/$', views.LivrosDelete.as_view(), name='deletar'),
	 #url(r'^(?P<categoria>[\w-]+)$',views.ProdutosListarCategoria.as_view(), name = 'listar-produtos-categoria'),
]