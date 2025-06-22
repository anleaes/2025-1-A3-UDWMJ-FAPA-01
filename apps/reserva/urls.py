from django.urls import path
from . import views

app_name = 'reserva'

urlpatterns = [
    path('adicionar/', views.add_reservas, name='add_reservas'),
    path('', views.list_reservas, name='list_reservas'),
    path('editar/<int:id_reserva>/', views.edit_reservas, name='edit_reservas'),
    path('excluir/<int:id_reserva>/', views.delete_reservas, name='delete_reservas'),
    path('cancelar/<int:id_reserva>/', views.cancelar_reserva, name='cancelar_reserva'),
]