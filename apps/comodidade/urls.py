from django.urls import path
from . import views

app_name = 'comodidade' 
urlpatterns = [
 
    path('adicionar/', views.add_comodidades, name='add_comodidades'),
    path('', views.list_comodidades, name='list_comodidades'),
    path('editar/<int:id_comodidade>/', views.edit_comodidades, name='edit_comodidades'),
    path('excluir/<int:id_comodidade>/', views.delete_comodidades, name='delete_comodidades'),
]