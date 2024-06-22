# distribuidores/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.DistribuidorListView.as_view(), name='distribuidor-list'),
    path('add/', views.DistribuidorCreateView.as_view(), name='distribuidor-add'),
    path('<int:pk>/edit/', views.DistribuidorUpdateView.as_view(), name='distribuidor-edit'),
    path('<int:pk>/delete/', views.DistribuidorDeleteView.as_view(), name='distribuidor-delete'),
]
