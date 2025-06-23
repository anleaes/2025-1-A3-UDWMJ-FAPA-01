from django.shortcuts import render, redirect, get_object_or_404
from .models import ItemReserva
from .forms import ItemReservaForm
from reserva.models import Reserva

def add_item_reserva(request, reserva_id=None):
    template_name = 'item_reserva/add_item_reserva.html'
    context = {}
    initial_data = {}

    if reserva_id:
        reserva = get_object_or_404(Reserva, id=reserva_id)
        initial_data['reserva'] = reserva.id
        context['reserva_pai'] = reserva

    if request.method == 'POST':
        form = ItemReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_reserva:list_itens_reserva_by_reserva', reserva_id=form.cleaned_data['reserva'].id)
        form = ItemReservaForm(initial=initial_data)
    
    context['form'] = form
    return render(request, template_name, context)

def list_itens_reserva(request):
    template_name = 'item_reserva/list_itens_reserva.html'
    itens_reserva = ItemReserva.objects.all()
    context = {
        'itens_reserva': itens_reserva
    }
    return render(request, template_name, context)

def list_itens_reserva_by_reserva(request, reserva_id):
    template_name = 'item_reserva/list_itens_reserva.html'
    reserva = get_object_or_404(Reserva, id=reserva_id)
    itens_reserva = ItemReserva.objects.filter(reserva=reserva)
    context = {
        'itens_reserva': itens_reserva,
        'reserva_pai': reserva
    }
    return render(request, template_name, context)

def edit_item_reserva(request, pk):
    template_name = 'item_reserva/add_item_reserva.html'
    context = {}
    item_reserva = get_object_or_404(ItemReserva, pk=pk)
    if request.method == 'POST':
        form = ItemReservaForm(request.POST, instance=item_reserva)
        if form.is_valid():
            form.save()
            return redirect('item_reserva:list_itens_reserva_by_reserva', reserva_id=item_reserva.reserva.id)

    form = ItemReservaForm(instance=item_reserva)
    context['form'] = form
    context['reserva_pai'] = item_reserva.reserva
    return render(request, template_name, context)

def delete_item_reserva(request, pk):
    item_reserva = get_object_or_404(ItemReserva, pk=pk)
    reserva_id = item_reserva.reserva.id
    item_reserva.delete()
    return redirect('item_reserva:list_itens_reserva_by_reserva', reserva_id=reserva_id)