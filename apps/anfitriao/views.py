from django.shortcuts import render, redirect
from .forms import AnfitriaoForm
from .models import Anfitriao

def add_anfitriao(request):
    template_name = 'anfitriao/add_anfitriao.html'
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