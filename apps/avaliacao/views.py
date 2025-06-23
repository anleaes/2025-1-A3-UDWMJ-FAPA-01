from django.shortcuts import render, redirect, get_object_or_404
from .models import Avaliacao
from .forms import AvaliacaoForm
from reserva.models import Reserva

def add_avaliacao(request, reserva_id=None):
    template_name = 'avaliacao/add_avaliacao.html'
    context = {}
    initial_data = {}
    if reserva_id:
        reserva = get_object_or_404(Reserva, id=reserva_id)
        if hasattr(reserva, 'avaliacao'): 
            return redirect('avaliacao:edit_avaliacao', pk=reserva.avaliacao.pk)
        initial_data['reserva'] = reserva.id
        context['reserva_associada'] = reserva 

    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            avaliacao = form.save()
            return redirect('avaliacao:list_avaliacoes')
    form = AvaliacaoForm(initial=initial_data)
    context['form'] = form
    return render(request, template_name, context)

def list_avaliacoes(request):
    template_name = 'avaliacao/list_avaliacoes.html'
    avaliacoes = Avaliacao.objects.all().select_related('reserva__imovel', 'reserva__hospede')
    context = {
        'avaliacoes': avaliacoes
    }
    return render(request, template_name, context)

def edit_avaliacao(request, pk):
    template_name = 'avaliacao/add_avaliacao.html'
    context = {}
    avaliacao = get_object_or_404(Avaliacao, pk=pk)
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST, instance=avaliacao)
        if form.is_valid():
            form.save()
            return redirect('avaliacao:list_avaliacoes')
    form = AvaliacaoForm(instance=avaliacao)
    context['form'] = form
    context['reserva_associada'] = avaliacao.reserva 
    return render(request, template_name, context)

def delete_avaliacao(request, pk):
    avaliacao = get_object_or_404(Avaliacao, pk=pk)
    avaliacao.delete()
    return redirect('avaliacao:list_avaliacoes')