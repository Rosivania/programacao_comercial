from django import forms
from .models import *

class FormularioSolicitacao(forms.ModelForm):
    """
    Formulario para o model Livro
    """
    class Meta:
        model = Solicitacao
        exclude = [ 'usuario_solicitado', 'usuario_solicitante','data_devolucao','devolvido']
    def __init__(self, *args, **kwargs):
        super(FormularioSolicitacao, self).__init__(*args, **kwargs)