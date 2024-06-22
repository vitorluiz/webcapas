# ponto_venda/models.py

from django.db import models
from distribuidores.models import Distribuidor

class PontoVenda(models.Model):
    cod_ponto = models.CharField(max_length=4, verbose_name="Cod. PONTO")
    ponto = models.CharField(max_length=150, verbose_name="PONTO")
    rota = models.CharField(max_length=5, verbose_name="ROTA")
    endereco = models.CharField(max_length=200, verbose_name="ENDEREÇO")
    bairro_cidade = models.CharField(max_length=100, verbose_name="BAIRRO/CIDADE")
    telefone = models.CharField(max_length=40, verbose_name="TELEFONE")
    observacoes = models.TextField(blank=True, null=True, verbose_name="Observações")
    distribuidor = models.ForeignKey(Distribuidor, on_delete=models.CASCADE, verbose_name="Distribuidor")
    status = models.BooleanField(default=True, verbose_name="Status")

    def __str__(self):
        return f"{self.ponto} ({self.cod_ponto})"
