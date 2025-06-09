from django.shortcuts import render, redirect, get_object_or_404
from .forms import HospedeForm
from .models import Hospede

def add_hospedes(request):
    template_name = 'hospedes/add_hospedes.html'
    context = {}
    if request.method == 'POST':
        form = HospedeForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('/hospede')
    form = HospedeForm()
    context['form'] = form
    return render(request, template_name, context)


def list_hospedes(request):
    template_name = 'hospedes/list_hospedes.html'
    hospedes = Hospede.objects.filter()
    context = {
        'hospedes': hospedes
    }
    return render(request, template_name, context)

def edit_hospedes(request, id_hospede):
    template_name = 'hospedes/add_hospedes.html'
    context ={}
    hospede = get_object_or_404(Hospede, id=id_hospede)
    if request.method == 'POST':
        form = HospedeForm(request.POST, instance=hospede)
        if form.is_valid():
            form.save()
            return redirect('hospedes:list_hospedes')
    form = HospedeForm(instance=hospede)
    context['form'] = form
    return render(request, template_name, context)



def delete_hospedes(request, id_hospede):
    hospede = Hospede.objects.get(id=id_hospede)
    hospede.delete()
    return redirect('hospedes:hospedes')