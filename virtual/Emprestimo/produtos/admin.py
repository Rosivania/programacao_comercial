from django.contrib import admin
from produtos.models import*

class ProdutoAdmin(admin.ModelAdmin):
	"""
	Admin para o model Produto
	"""
	list_display = ['nome','categoria','descricao','image']
	search_fields =['nome','categoria']
	list_filter=['categoria']

admin.site.register(Produto, ProdutoAdmin)
