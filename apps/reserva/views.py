from django.shortcuts import render, redirect, get_object_or_404
from .models import Reserva
from .forms import ReservaForm, ItemReservaFormSet

def add_reservas(request):
    template_name = 'reservas/add_reservas.html'
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        formset = ItemReservaFormSet(request.POST, request.FILES, prefix='itens')

        if form.is_valid() and formset.is_valid():
            reserva = form.save(commit=False)
            reserva.save()
            form.save_m2m()

            formset.instance = reserva
            formset.save()

            return redirect('reserva:list_reservas')
    else:
        form = ReservaForm()
        formset = ItemReservaFormSet(prefix='itens')

    context = {'form': form, 'formset': formset}
    return render(request, template_name, context)


def list_reservas(request):
    template_name = 'reservas/list_reservas.html'
    reservas = Reserva.objects.all().prefetch_related('itens_reserva__servico_adicional')
    context = {'reservas': reservas}
    return render(request, template_name, context)


def edit_reservas(request, id_reserva):
    template_name = 'reservas/add_reservas.html'
    reserva = get_object_or_404(Reserva, id=id_reserva)

    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        formset = ItemReservaFormSet(request.POST, request.FILES, instance=reserva, prefix='itens')

        if form.is_valid() and formset.is_valid():
            reserva = form.save()
            formset.instance = reserva
            formset.save()

            return redirect('reserva:list_reservas')
    else:
        form = ReservaForm(instance=reserva)
        formset = ItemReservaFormSet(instance=reserva, prefix='itens')

    context = {'form': form, 'formset': formset}
    return render(request, template_name, context)


def delete_reservas(request, id_reserva):
    reserva = get_object_or_404(Reserva, id=id_reserva)
    reserva.delete()
    return redirect('reserva:list_reservas')


def cancelar_reserva(request, id_reserva):
    reserva = get_object_or_404(Reserva, id=id_reserva)
    if request.method == 'POST':
        reserva.cancelar()
        return redirect('reserva:list_reservas')
    return render(request, 'reservas/confirm_cancelar_reserva.html', {'reserva': reserva})
