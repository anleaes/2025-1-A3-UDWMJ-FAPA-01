from django.shortcuts import render, redirect, get_object_or_404
from .models import Pagamento 
from .forms import PagamentoForm 
from reserva.models import Reserva 

def add_pagamento(request, reserva_id=None):
    template_name = 'pagamento/add_pagamento.html'
    context = {}
    initial_data = {}

    if reserva_id:
        reserva = get_object_or_404(Reserva, id=reserva_id)
        if hasattr(reserva, 'pagamento'):
            return redirect('pagamento:edit_pagamento', pk=reserva.pagamento.pk)
        initial_data['reserva'] = reserva.id
        initial_data['valor'] = reserva.preco_total 
        context['reserva_associada'] = reserva

    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            pagamento = form.save(commit=False)
            pagamento.save() 
            pagamento.processarPagamento() 
            return redirect('pagamento:list_pagamentos')

    form = PagamentoForm(initial=initial_data)
    context['form'] = form
    return render(request, template_name, context)

def list_pagamentos(request):
    template_name = 'pagamento/list_pagamentos.html'
    pagamentos = Pagamento.objects.all().select_related('reserva__imovel', 'reserva__hospede')
    context = {
        'pagamentos': pagamentos
    }
    return render(request, template_name, context)

def edit_pagamento(request, pk):
    template_name = 'pagamento/add_pagamento.html'
    context = {}
    pagamento = get_object_or_404(Pagamento, pk=pk)

    if request.method == 'POST':
        form = PagamentoForm(request.POST, instance=pagamento)
        if form.is_valid():
            pagamento = form.save(commit=False)
            pagamento.save() 
            pagamento.processarPagamento()
            return redirect('pagamento:list_pagamentos')
    form = PagamentoForm(instance=pagamento)
    context['form'] = form
    context['reserva_associada'] = pagamento.reserva
    return render(request, template_name, context)

def delete_pagamento(request, pk):
    pagamento = get_object_or_404(Pagamento, pk=pk)
    pagamento.delete()
    return redirect('pagamento:list_pagamentos')