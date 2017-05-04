from django.contrib import admin
from livros.models import*
class LivroAdmin(admin.ModelAdmin):
	"""
	Admin para o model Livro
	"""
	list_display = ['titulo','ano','categoria','image']
	search_fields =['titulo','categoria']
	list_filter=['categoria']

admin.site.register(Livro, LivroAdmin)

