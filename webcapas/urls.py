# webcapas/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('edicoes/', include('edicoes.urls')),
    path('distribuidores/', include('distribuidores.urls')),
    path('pontosvenda/', include('ponto_venda.urls')),
    path('distribuicoes/', include('distribuicoes.urls')),


]
