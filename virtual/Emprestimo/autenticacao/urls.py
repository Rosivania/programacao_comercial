from django.conf.urls import url
from autenticacao import views

urlpatterns = [
	url(r'^$',views.Autenticacao.as_view(),name='autenticacao-login'),
	url(r'^livros/sair/', views.Logout.as_view(), name='sair'),
	url(r'^livros/lista_Pessoal/sair/', views.Logout.as_view(), name='sair'),
	url(r'^livros/solicitacao/sair/', views.Logout.as_view(), name='sair'),
	#url(r'^sair/', views.Logout.as_view(), name='sair'),
	#url(r'^logado/', views.Index.as_view(), name='logado'),

]