# edicoes/views.py

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Edicao

class EdicaoListView(ListView):
    model = Edicao

class EdicaoCreateView(CreateView):
    model = Edicao
    fields = ['data_sorteio', 'etapa', 'valor', 'tipo']
    success_url = reverse_lazy('edicao-list')

class EdicaoUpdateView(UpdateView):
    model = Edicao
    fields = ['data_sorteio', 'etapa', 'valor', 'tipo']
    success_url = reverse_lazy('edicao-list')

class EdicaoDeleteView(DeleteView):
    model = Edicao
    success_url = reverse_lazy('edicao-list')
