from django.shortcuts import render, redirect, get_object_or_404
from .models import ComodidadeImovel
from .forms import ComodidadeImovelForm

def add_comodidade_imovel(request):
    template_name = 'comodidade_imovel/add_comodidade_imovel.html'
    context = {}
    if request.method == 'POST':
        form = ComodidadeImovelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comodidade_imovel:list_comodidade_imovel')

    form = ComodidadeImovelForm()
    context['form'] = form
    return render(request, template_name, context)

def list_comodidade_imovel(request):
    template_name = 'comodidade_imovel/list_comodidade_imovel.html'
    comodidades_imoveis = ComodidadeImovel.objects.all()
    context = {
        'comodidades_imoveis': comodidades_imoveis
    }
    return render(request, template_name, context)

def edit_comodidade_imovel(request, pk):
    template_name = 'comodidade_imovel/add_comodidade_imovel.html'
    context = {}
    comodidade_imovel = get_object_or_404(ComodidadeImovel, pk=pk)
    if request.method == 'POST':
        form = ComodidadeImovelForm(request.POST, instance=comodidade_imovel)
        if form.is_valid():
            form.save()
            return redirect('comodidade_imovel:list_comodidade_imovel')

    form = ComodidadeImovelForm(instance=comodidade_imovel)
    context['form'] = form
    return render(request, template_name, context)

def delete_comodidade_imovel(request, pk):
    comodidade_imovel = get_object_or_404(ComodidadeImovel, pk=pk)
    comodidade_imovel.delete()
    return redirect('comodidade_imovel:list_comodidade_imovel')