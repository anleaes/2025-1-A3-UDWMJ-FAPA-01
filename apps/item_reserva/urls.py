from django.urls import path
from . import views

app_name = 'item_reserva'

urlpatterns = [
    path('', views.list_itens_reservas, name='list_reservas'),
]