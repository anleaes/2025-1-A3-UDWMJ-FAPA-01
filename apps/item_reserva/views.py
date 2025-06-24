from django.shortcuts import render, redirect, get_object_or_404
from .forms import ItemReserva
from .models import ItemReserva

def list_itens_reservas(request):
    template_name = 'item_reservas/list_itens_reservas.html'
    itens_reserva = ItemReserva.objects.filter()
    context = {
        'itens_reserva': itens_reserva
    }
    return render(request, template_name, context)