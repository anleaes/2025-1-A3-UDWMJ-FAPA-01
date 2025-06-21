from django.urls import path
from . import views

app_name = 'servico_adicional'

urlpatterns = [
    path('adicionar/', views.add_servicos_adicionais, name='add_servicos_adicionais'),
    path('', views.list_servicos_adicionais, name='list_servicos_adicionais'),
    path('editar/<int:id_servico_adicional>/', views.edit_servicos_adicionais, name='edit_servicos_adicionais'),
    path('excluir/<int:id_servico_adicional>/', views.delete_servicos_adicionais, name='delete_servicos_adicionais'),
]