# distribuicoes/views.py

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Distribuicao

import csv
from django.shortcuts import render, redirect
from .models import Distribuicao
from ponto_venda.models import PontoVenda
from edicoes.models import Edicao
from .forms import DistribuicaoCSVForm


class DistribuicaoListView(ListView):
    model = Distribuicao

class DistribuicaoCreateView(CreateView):
    model = Distribuicao
    fields = ['ponto', 'titulo_inicial', 'titulo_final', 'titulo_qtd', 'edicao']
    success_url = reverse_lazy('distribuicao-list')

class DistribuicaoUpdateView(UpdateView):
    model = Distribuicao
    fields = ['ponto', 'titulo_inicial', 'titulo_final', 'titulo_qtd', 'edicao']
    success_url = reverse_lazy('distribuicao-list')

class DistribuicaoDeleteView(DeleteView):
    model = Distribuicao
    success_url = reverse_lazy('distribuicao-list')

def importar_distribuicao_csv(request):
    if request.method == 'POST':
        form = DistribuicaoCSVForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo_csv = request.FILES['arquivo_csv']
            reader = csv.DictReader(arquivo_csv.read().decode('utf-8').splitlines(), delimiter=';')
            for row in reader:
                ponto_venda = PontoVenda.objects.get(cod_ponto=row['Cod.'])
                edicao = Edicao.objects.get(pk=1)  # Exemplo de vinculação com uma edição específica
                Distribuicao.objects.create(
                    ponto=ponto_venda,
                    cod_inicial=row['Inicial'],
                    cod_final=row['Final'],
                    qtd=int(row['Qtd.']),
                    edicao=edicao
                )
            return redirect('distribuicao-list')
    else:
        form = DistribuicaoCSVForm()
    return render(request, 'distribuicoes/importar_distribuicao.html', {'form': form})