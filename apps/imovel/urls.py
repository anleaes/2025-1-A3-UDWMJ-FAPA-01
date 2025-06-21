from django.urls import path
from . import views

app_name = 'imovel'

urlpatterns = [
    path('adicionar/', views.add_imoveis, name='add_imoveis'),
    path('', views.list_imoveis, name='list_imoveis'),
    path('editar/<int:id_imovel>/', views.edit_imoveis, name='edit_imoveis'),
    path('excluir/<int:id_imovel>/', views.delete_imoveis, name='delete_imoveis'),
]
