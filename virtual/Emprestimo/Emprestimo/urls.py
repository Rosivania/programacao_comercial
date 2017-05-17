from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from autenticacao import views

from livros.views import NotFoundView

handler404 = NotFoundView.get_rendered_view()

admin.autodiscover()

urlpatterns = [
	url(r'^',include('autenticacao.urls', namespace = 'autenticacao-login')),
    #url(r'^produtos/', include('produtos.urls')),
    url(r'^livros/', include('livros.urls')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
