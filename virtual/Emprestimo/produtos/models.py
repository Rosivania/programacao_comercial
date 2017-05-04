from django.db import models
from produtos.const import *
from PIL import Image




class Produto(models.Model):
	
    nome = models.CharField('Nome', max_length=100)
    categoria = models.SmallIntegerField(choices=CATEGORIAS)
    status = models.BooleanField(choices=BOOL_CHOICES)
    #status = models.BooleanField(default=False)
    descricao = models.TextField('Descrição', blank=True)
    image = models.ImageField(upload_to='images', blank=True)
    def __str__(self):
    	return '{0} - {1} - {2}'.format(self.nome,  self.get_categoria_display(), self.descricao)
