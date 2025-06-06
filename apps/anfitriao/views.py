from django.shortcuts import render, redirect, get_object_or_404
from .forms import AnfitriaoForm
from .models import Anfitriao

def add_anfitrioes(request):
    template_name = 'anfitrioes/add_anfitrioes.html'
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


def edit_anfitrioes(request, id_anfitriao):
    template_name = 'anfitrioes/add_anfitrioes.html'
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

def list_anfitrioes(request):
    template_name = 'anfitrioes/list_anfitrioes.html'
    categories = Anfitriao.objects.filter()
    context = {
        'anfitrioes': anfitrioes
    }
    return render(request, template_name, context)
