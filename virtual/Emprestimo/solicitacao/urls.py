from django.conf.urls import url, include
from django.contrib import admin
#from apps.jogo import views
from solicitacao import views
from django.contrib.auth.decorators import login_required
app_name = 'solicitacao'
urlpatterns = [
    #url(r'^listar$', views.SolicitarList.as_view(), name='listar'),
    url(r'^solicitar$', views.SolicitacaoNew.as_view(), name='solicitar'),
    #url(r'^devolver$', views.Devolver.as_view(), name='devolver'),
]