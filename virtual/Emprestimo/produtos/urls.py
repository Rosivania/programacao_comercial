from django.conf.urls import url
from produtos import views
app_name = 'produtos'
urlpatterns = [
	#url(r'^$', views.ProdutosList.as_view(), name='listar-produtos'),
	 url(r'^novo/$', views.ProdutosNew.as_view(), name='novo'),
	 url(r'^(?P<pk>[0-9]+)/$', views.ProdutosEdit.as_view(), name='editar-produto'),
	 url(r'^excluir/(?P<pk>[0-9]+)/$', views.ProdutosDelete.as_view(), name='deletar-produto'),
	 #url(r'^(?P<categoria>[\w-]+)$',views.ProdutosListarCategoria.as_view(), name = 'listar-produtos-categoria'),
]