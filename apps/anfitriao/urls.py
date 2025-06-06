from django.urls import path
from . import views

app_name = 'anfitrioes'

urlpatterns = [
    path('adicionar/', views.add_anfitrioes, name='add_anfitrioes'),
    path('', views.list_anfitrioes, name='list_categories'),
    path('editar/<int:id_anfitriao>/', views.edit_anfitrioes, name='edit_anfitrioes'),
    path('excluir/<int:id_anfitriao>/', views.delete_anfitrioes, name='delete_anfitrioes'),
]