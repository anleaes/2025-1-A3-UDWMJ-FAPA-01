from django.urls import path
from . import views

app_name = 'pagamento'

urlpatterns = [
    path('adicionar/', views.add_pagamento, name='add_pagamento'),
    path('', views.list_pagamentos, name='list_pagamentos'),
    path('editar/<int:pk>/', views.edit_pagamento, name='edit_pagamento'),
    path('excluir/<int:pk>/', views.delete_pagamento, name='delete_pagamento'),
]