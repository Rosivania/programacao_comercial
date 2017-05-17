from django.db import models
from django.contrib.auth.models import User
from livros.models import Livro
import datetime

class Solicitacao(models.Model):

    livro_solicitado = models.ManyToManyField(Livro, limit_choices_to = {'disponivel':True})
    usuario_solicitante = models.ForeignKey(User, related_name='solicitante')
    data_emprestimo = models.DateTimeField('Data de Empréstimo', auto_now_add=True)
    #prazo_devolucao = models.DateTimeField('Prazo para Devolução', null=True)
    data_devolucao = models.DateTimeField('Data de Devolução', null=True)
    devolvido = models.BooleanField(default=False)
    usuario_solicitado = models.ForeignKey(User, related_name='solicitado')
    #usuario_devolucao = models.ForeignKey(User, related_name="usuario_devolucao", null=True)

    def __str__(self):
        return '{0} - {1} - {2} - {3} - {4} - {5}'.format(
            self.livro_solicitado, 
            self.data_emprestimo,
            self.data_devolucao,
            self.devolvido,
            self.usuario_solicitante, 
            self.usuario_solicitado
            )

