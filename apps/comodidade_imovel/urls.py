from django.urls import path
from . import views

app_name = 'comodidade_imovel'

urlpatterns = [
    path('adicionar/', views.add_comodidade_imovel, name='add_comodidade_imovel'),
    path('', views.list_comodidade_imovel, name='list_comodidade_imovel'),
    path('editar/<int:pk>/', views.edit_comodidade_imovel, name='edit_comodidade_imovel'),
    path('excluir/<int:pk>/', views.delete_comodidade_imovel, name='delete_comodidade_imovel'),
]