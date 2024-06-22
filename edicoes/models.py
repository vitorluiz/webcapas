# edicoes/models.py

from django.db import models

class Edicao(models.Model):
    TIPOS = [
        ('Simples', 'Simples'),
        ('Dupla', 'Dupla'),
        ('Especial', 'Especial'),
    ]
    
    data_sorteio = models.DateField()
    etapa = models.CharField(max_length=3)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=20, choices=TIPOS)

    def __str__(self):
        return f"{self.etapa} ({self.data_sorteio})"
