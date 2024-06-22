# edicoes/admin.py

from django.contrib import admin
from .models import Edicao

@admin.register(Edicao)
class EdicaoAdmin(admin.ModelAdmin):
    list_display = ('data_sorteio', 'etapa', 'valor', 'tipo')
    search_fields = ('etapa',)
