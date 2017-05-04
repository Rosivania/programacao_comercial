from django.db import models

class Veiculo(models.Model):
	marca = models.CharField(max_length=100)
	modelo = models.CharField(max_length=100)
	ano_fabricacao = models.IntegerField()
	modelo_fabricacao = models.IntegerField()
	combustivel = models.SmallIntegerField(choices=[(1, 'ETANOL'), (2, 'FLEX'), (3, 'GASOLINA')])

	def __str__(self):
		return '{} {} - {} ({}/{})'.format(self.pk, self.marca, self.modelo, self.ano_fabricacao, self.modelo_fabricacao)
