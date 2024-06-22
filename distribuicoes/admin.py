# distribuicoes/admin.py

from django.contrib import admin
from .models import Distribuicao

@admin.register(Distribuicao)
class DistribuicaoAdmin(admin.ModelAdmin):
    list_display = ('ponto', 'rota', 'titulo_inicial', 'titulo_final', 'titulo_qtd', 'edicao')
    search_fields = ('ponto__ponto', 'ponto__rota', 'titulo_inicial', 'titulo_final')
    list_filter = ('edicao','ponto__rota')


