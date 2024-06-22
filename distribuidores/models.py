# distribuidores/models.py

from django.db import models

class Distribuidor(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Distribuidor")
    telefone = models.CharField(max_length=20, verbose_name="Tel. Distribuidor")
    

    def __str__(self):
        return self.nome
