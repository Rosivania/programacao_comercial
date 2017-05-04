from django import forms
from .models import *

class FormularioProduto(forms.ModelForm):
    """
    Formulario para o model Produto
    """
    class Meta:
        model = Produto
        exclude = []
    def __init__(self, *args, **kwargs):
        super(FormularioProduto, self).__init__(*args, **kwargs)
        self.fields['nome'].label = 'Nome:'
        self.fields['nome'].widget.attrs['class'] = 'form-control'
        #self.fields['nome'].widget.attrs['placeholder'] = 'Nome do produto'
        #self.fields['nome'].widget.attrs['required'] = 'required'

        self.fields['categoria'].label = 'Categoria:'
        #self.fields['categoria'].widget.attrs['class'] = 'form-control'
        #self.fields['categoria'].widget.attrs['placeholder'] = 'Categoria do Produto'
        self.fields['categoria'].widget.attrs['required'] = 'required'

        self.fields['status'].label = 'Status:'
        #self.fields['categoria'].widget.attrs['class'] = 'form-control'
        #self.fields['categoria'].widget.attrs['placeholder'] = 'Categoria do Produto'
        #self.fields['status'].widget.attrs['required'] = 'required'

        # widgets = {
        #     'status': forms.RadioSelect
        # }
        #self.fields['status'].widget = forms.RadioSelect(choices=BOOL_CHOICES)

        self.fields['descricao'].label = 'Descrição:'
        self.fields['descricao'].widget.attrs['class'] = 'form-control'
        #self.fields['descricao'].widget.attrs['placeholder'] = 'Descrição do Produto'
        self.fields['descricao'].widget.attrs['required'] = 'required'

        self.fields['image'].label = 'Imagem:'
        self.fields['image'].widget.attrs['class'] = 'form-control'
        #self.fields['descricao'].widget.attrs['placeholder'] = 'Descrição do Produto'
        self.fields['image'].widget.attrs['required'] = 'required'
# class FormularioImagem(forms.ModelForm):

#     class Meta:
#         model = Imagem
#         fields = ['nome', 'imageFile']
# class ImageUploadForm(forms.Form):
#     """Image upload form."""
#     image = forms.ImageField()