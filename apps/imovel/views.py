from django.shortcuts import render, redirect, get_object_or_404
from .models import Imovel
from .forms import ImovelForm

def add_imoveis(request):
    template_name = 'imovel/add_imoveis.html'
    context = {}
    if request.method == 'POST':
        form = ImovelForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('/imovel')
    form = ImovelForm()
    context['form'] = form
    return render(request, template_name, context)


def list_imoveis(request):
    template_name = 'imovel/list_imoveis.html'
    imoveis = Imovel.objects.all()
    context = {
        'imoveis': imoveis
    }
    return render(request, template_name, context)


def edit_imoveis(request, id_imovel):
    template_name = 'imovel/add_imoveis.html'
    context = {}
    imovel = get_object_or_404(Imovel, id=id_imovel)
    if request.method == 'POST':
        form = ImovelForm(request.POST, instance=imovel)
        if form.is_valid():
            form.save()
            return redirect('imovel:list_imoveis')
    form = ImovelForm(instance=imovel)
    context['form'] = form
    return render(request, template_name, context)


def delete_imoveis(request, id_imovel):
    imovel = Imovel.objects.get(id=id_imovel)
    imovel.delete()
    return redirect('imovel:list_imoveis')

