from django.urls import path
from . import views

app_name = 'avaliacao'

urlpatterns = [
    path('adicionar/', views.add_avaliacao, name='add_avaliacao'),
    path('adicionar/<int:reserva_id>/', views.add_avaliacao, name='add_avaliacao_for_reserva'),
    path('', views.list_avaliacoes, name='list_avaliacoes'),
    path('editar/<int:pk>/', views.edit_avaliacao, name='edit_avaliacao'),
    path('excluir/<int:pk>/', views.delete_avaliacao, name='delete_avaliacao'),
]