from django.shortcuts import render, redirect, get_object_or_404
from .models import Reserva
from .forms import ReservaForm

def add_reservas(request):
    template_name = 'reservas/add_reservas.html'
    context = {}
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.calcular_preco_total()
            reserva.save()
            form.save_m2m()
            return redirect('/reserva')
    form = ReservaForm()
    context['form'] = form
    return render(request, template_name, context)

def list_reservas(request):
    template_name = 'reservas/list_reservas.html'
    reservas = Reserva.objects.filter()
    context = {
        'reservas': reservas
    }
    return render(request, template_name, context)

def edit_reservas(request, id_reserva):
    template_name = 'reservas/add_reservas.html'
    context = {}
    reserva = get_object_or_404(Reserva, id=id_reserva)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            reserva_editada = form.save(commit=False)
            reserva_editada.calcular_preco_total()
            reserva_editada.save()
            form.save_m2m()
            return redirect('reserva:list_reservas')

    form = ReservaForm(instance=reserva)
    context['form'] = form
    return render(request, template_name, context)

def delete_reservas(request, id_reserva):
    reserva = get_object_or_404(Reserva, id=id_reserva) 
    reserva.delete()
    return redirect('reserva:list_reservas')

def cancelar_reserva(request, id_reserva):
    reserva = get_object_or_404(Reserva, id=id_reserva)
    if request.method == 'POST':
        if reserva.cancelar():
            pass
        else:
            pass
        return redirect('reserva:list_reservas')
    return render(request, 'reservas/confirm_cancelar_reserva.html', {'reserva': reserva})