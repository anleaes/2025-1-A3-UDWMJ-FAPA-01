from django.shortcuts import render, redirect, get_object_or_404
from .forms import AnfitriaoForm
from .models import Anfitriao

def add_anfitriao(request):
    template_name = 'anfitrioes/add_anfitriao.html'
    context = {}
    if request.method == 'POST':
        form = AnfitriaoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('core:home')
    form = AnfitriaoForm()
    context['form'] = form
    return render(request, template_name, context)


def edit_anfitriao(request, id_anfitriao):
    template_name = 'anfitrioes/add_anfitriao.html'
    context ={}
    anfitriao = get_object_or_404(anfitriao, id=id_anfitriao)
    if request.method == 'POST':
        form = AnfitriaoForm(request.POST, instance=anfitriao)
        if form.is_valid():
            form.save()
            return redirect('anfitrioes:list_anfitrioes')
    form = AnfitriaoForm(instance=anfitriao)
    context['form'] = form
    return render(request, template_name, context)