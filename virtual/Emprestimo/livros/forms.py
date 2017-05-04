from django import forms
from .models import *

class FormularioLivro(forms.ModelForm):
    """
    Formulario para o model Livro
    """
    class Meta:
        model = Livro
        exclude = ['usuario']
    def __init__(self, *args, **kwargs):
        super(FormularioLivro, self).__init__(*args, **kwargs)