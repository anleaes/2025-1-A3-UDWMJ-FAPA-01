from django.shortcuts import render, redirect, get_object_or_404
from .models import ServicoAdicional
from .forms import ServicoAdicionalForm

def add_servicos_adicionais(request): 
    template_name = 'servicos_adicionais/add_servicos_adicionais.html'
    context = {}
    if request.method == 'POST':
        form = ServicoAdicionalForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m() 
            return redirect('/servico_adicional') 
    form = ServicoAdicionalForm()
    context['form'] = form
    return render(request, template_name, context)

def list_servicos_adicionais(request):   
    template_name = 'servicos_adicionais/list_servicos_adicionais.html'
    servicos_adicionais = ServicoAdicional.objects.filter() 
    context = {
        'servicos_adicionais': servicos_adicionais
    }
    return render(request, template_name, context)

def edit_servicos_adicionais(request, id_servico_adicional):  
    template_name = 'servicos_adicionais/add_servicos_adicionais.html'
    context = {}
    servico_adicional = get_object_or_404(ServicoAdicional, id=id_servico_adicional)
    if request.method == 'POST':
        form = ServicoAdicionalForm(request.POST, instance=servico_adicional)
        if form.is_valid():
            form.save()
            return redirect('servico_adicional:list_servicos_adicionais') 
    form = ServicoAdicionalForm(instance=servico_adicional)
    context['form'] = form
    return render(request, template_name, context)

def delete_servicos_adicionais(request, id_servico_adicional): 
    servico_adicional = ServicoAdicional.objects.get(id=id_servico_adicional) 
    servico_adicional.delete()
    return redirect('servico_adicional:list_servicos_adicionais')