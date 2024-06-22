# ponto_venda/views.py

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import PontoVenda

class PontoVendaListView(ListView):
    model = PontoVenda

class PontoVendaCreateView(CreateView):
    model = PontoVenda
    fields = ['cod_ponto', 'ponto', 'rota', 'endereco', 'bairro_cidade', 'telefone', 'distribuidor', 'status', 'observacoes']
    success_url = reverse_lazy('pontovenda-list')

class PontoVendaUpdateView(UpdateView):
    model = PontoVenda
    fields = ['cod_ponto', 'ponto', 'rota', 'endereco', 'bairro_cidade', 'telefone', 'distribuidor', 'status', 'observacoes']
    success_url = reverse_lazy('pontovenda-list')

class PontoVendaDeleteView(DeleteView):
    model = PontoVenda
    success_url = reverse_lazy('pontovenda-list')
