from django.db import models
from livros.const import *
from PIL import Image
from django.contrib.auth.models import User



class Livro(models.Model):
	
    titulo = models.CharField('Titulo', max_length=100)
    categoria = models.SmallIntegerField(choices=CATEGORIAS)
    editora = models.CharField('Editora', max_length=100)
    autor = models.CharField('Autor', max_length=100)
    ano = models.IntegerField()
    idioma = models.CharField('Idioma', max_length=30)
    image = models.ImageField('Imagem',upload_to='livros', blank=True)
    #added_by = models.ForeignKey(User, null=True, blank=True)
    usuario = models.ForeignKey(User, related_name='livros')
    disponivel = models.BooleanField(default=True)
    def __str__(self):
    	return '{0} - {1} - {2} - {3} - {4} - {5} - {6}'.format(
            self.titulo, 
            self.get_categoria_display(),
            self.editora, self.autor,
            self.ano, 
            self.idioma,
            self.image
            )


