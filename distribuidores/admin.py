# distribuidores/admin.py

from django.contrib import admin
from .models import Distribuidor

@admin.register(Distribuidor)
class DistribuidorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone')
    search_fields = ('nome',)
