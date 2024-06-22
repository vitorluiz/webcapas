# edicoes/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.EdicaoListView.as_view(), name='edicao-list'),
    path('add/', views.EdicaoCreateView.as_view(), name='edicao-add'),
    path('<int:pk>/edit/', views.EdicaoUpdateView.as_view(), name='edicao-edit'),
    path('<int:pk>/delete/', views.EdicaoDeleteView.as_view(), name='edicao-delete'),
]
