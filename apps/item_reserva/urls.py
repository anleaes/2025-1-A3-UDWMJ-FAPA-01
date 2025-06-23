from django.urls import path
from . import views

app_name = 'item_reserva'

urlpatterns = [
    path('adicionar/', views.add_item_reserva, name='add_item_reserva'),
    path('', views.list_itens_reserva, name='list_itens_reserva'),
    path('editar/<int:pk>/', views.edit_item_reserva, name='edit_item_reserva'),
    path('excluir/<int:pk>/', views.delete_item_reserva, name='delete_item_reserva'),
]