# distribuidores/views.py

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Distribuidor

class DistribuidorListView(ListView):
    model = Distribuidor

class DistribuidorCreateView(CreateView):
    model = Distribuidor
    fields = ['nome', 'telefone']
    success_url = reverse_lazy('distribuidor-list')

class DistribuidorUpdateView(UpdateView):
    model = Distribuidor
    fields = ['nome', 'telefone']
    success_url = reverse_lazy('distribuidor-list')

class DistribuidorDeleteView(DeleteView):
    model = Distribuidor
    success_url = reverse_lazy('distribuidor-list')
