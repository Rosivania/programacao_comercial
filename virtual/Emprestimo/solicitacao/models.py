from django.db import models
from django.contrib.auth.models import User

# class Solicitacao(models.Model):
#     livros_solicitados = models.ManyToManyField('Livro', limit_choices_to = {'disponivel':True})
#     #usuario = models.ForeignKey(User, related_name='solicitante')
#     data_emprestimo = models.DateTimeField('Data de Empréstimo', auto_now_add=True)
#     #prazo_devolucao = models.DateTimeField('Prazo para Devolução', null=True)
#     data_devolucao = models.DateTimeField('Data de Devolução', null=True)
#     devolvido = models.BooleanField(default=False)
#     usuario_emprestimo = models.ForeignKey(User, related_name="%(class)s_emprestimo", null=True)
#     usuario_devolucao = models.ForeignKey(User, related_name="%(class)s_devolucao", null=True)

#     def __unicode__(self):
#         return str(self.id)

