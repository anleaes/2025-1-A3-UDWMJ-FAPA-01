from django.shortcuts import render, redirect, get_object_or_404
from .models import ItemReserva
from .forms import ItemReservaForm

def add_item_reserva(request):
    template_name = 'item_reserva/add_item_reserva.html'
    context = {}
    if request.method == 'POST':
        form = ItemReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_reserva:list_itens_reserva') 

    form = ItemReservaForm()
    context['form'] = form
    return render(request, template_name, context)

def list_itens_reserva(request):
    template_name = 'item_reserva/list_itens_reserva.html'
    itens_reserva = ItemReserva.objects.all()
    context = {
        'itens_reserva': itens_reserva
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
            return redirect('item_reserva:list_itens_reserva') 
    form = ItemReservaForm(instance=item_reserva)
    context['form'] = form
    return render(request, template_name, context)

def delete_item_reserva(request, pk):
    item_reserva = get_object_or_404(ItemReserva, pk=pk)
    item_reserva.delete()
    return redirect('item_reserva:list_itens_reserva')