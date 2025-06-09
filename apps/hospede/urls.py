from django.urls import path
from . import views

app_name = 'hospedes'

urlpatterns = [
    path('adicionar/', views.add_hospedes, name='add_hospedes'),
    path('', views.list_hospedes, name='list_hospedes'),
    path('editar/<int:id_hospede>/', views.edit_hospedes, name='edit_hospedes'),
    path('excluir/<int:id_hospede>/', views.delete_hospedes, name='delete_hospedes'),
]