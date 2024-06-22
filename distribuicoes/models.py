# distribuicoes/models.py

from django.db import models
from edicoes.models import Edicao
from ponto_venda.models import PontoVenda

class Distribuicao(models.Model):
    ponto = models.ForeignKey(PontoVenda, on_delete=models.CASCADE, verbose_name="Ponto")
    rota = models.CharField(max_length=5, verbose_name="Rota")
    titulo_inicial = models.CharField(max_length=20, verbose_name="Titulo Inicial")
    titulo_final = models.CharField(max_length=20, verbose_name="Titulo Final")
    titulo_qtd = models.IntegerField(verbose_name="Quantidade")
    edicao = models.ForeignKey(Edicao, on_delete=models.CASCADE, verbose_name="Edição")

    def __str__(self):
        return f"{self.ponto.ponto} - {self.titulo_inicial} a {self.titulo_final}"

    @property
    def rota(self):
        return self.ponto.rota
