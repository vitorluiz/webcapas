# ponto_venda/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.PontoVendaListView.as_view(), name='pontovenda-list'),
    path('add/', views.PontoVendaCreateView.as_view(), name='pontovenda-add'),
    path('<int:pk>/edit/', views.PontoVendaUpdateView.as_view(), name='pontovenda-edit'),
    path('<int:pk>/delete/', views.PontoVendaDeleteView.as_view(), name='pontovenda-delete'),
]
