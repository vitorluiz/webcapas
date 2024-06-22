# distribuicoes/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.DistribuicaoListView.as_view(), name='distribuicao-list'),
    path('add/', views.DistribuicaoCreateView.as_view(), name='distribuicao-add'),
    path('<int:pk>/edit/', views.DistribuicaoUpdateView.as_view(), name='distribuicao-edit'),
    path('<int:pk>/delete/', views.DistribuicaoDeleteView.as_view(), name='distribuicao-delete'),
    path('importar/', views.importar_distribuicao_csv, name='distribuicao-importar'),
]
