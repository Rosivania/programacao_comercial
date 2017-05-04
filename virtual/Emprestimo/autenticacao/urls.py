from django.conf.urls import url
from autenticacao import views

urlpatterns = [
	url(r'^$',views.Autenticacao.as_view(),name='autenticacao-login'),
	url(r'^sair/', views.logout, name='sair'),
	#url(r'^sair/', views.Logout.as_view(), name='sair'),
	#url(r'^logado/', views.Index.as_view(), name='logado'),

]