# ponto_venda/admin.py

from django.contrib import admin
from .models import PontoVenda

@admin.register(PontoVenda)
class PontoVendaAdmin(admin.ModelAdmin):
    list_display = ('cod_ponto', 'ponto', 'rota', 'distribuidor', 'status')
    search_fields = ('ponto', 'cod_ponto', 'rota')
    list_filter = ('distribuidor', 'status')
