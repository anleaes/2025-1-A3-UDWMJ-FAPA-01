from django.shortcuts import render, redirect, get_object_or_404
from .models import Comodidade
from .forms import ComodidadeForm

def add_comodidades(request):
    template_name = 'comodidades/add_comodidades.html'
    context = {}
    if request.method == 'POST':
        form = ComodidadeForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False) 
            f.save()
            form.save_m2m()
            return redirect('/comodidade') 
    form = ComodidadeForm()
    context['form'] = form
    return render(request, template_name, context)

def list_comodidades(request):
    template_name = 'comodidades/list_comodidades.html'
    comodidades = Comodidade.objects.filter() 
    context = {
        'comodidades': comodidades
    }
    return render(request, template_name, context)

def edit_comodidades(request, id_comodidade):
    template_name = 'comodidades/add_comodidades.html'
    context = {}
    comodidade = get_object_or_404(Comodidade, id=id_comodidade) 
    if request.method == 'POST':
        form = ComodidadeForm(request.POST, instance=comodidade)
        if form.is_valid():
            form.save()
            return redirect('comodidade:list_comodidades')
    form = ComodidadeForm(instance=comodidade)
    context['form'] = form
    return render(request, template_name, context)

def delete_comodidades(request, id_comodidade):
    comodidade = Comodidade.objects.get(id=id_comodidade) 
    comodidade.delete()
    return redirect('comodidade:list_comodidades')
