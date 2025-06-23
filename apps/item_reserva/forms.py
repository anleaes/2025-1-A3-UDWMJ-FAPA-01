from django import forms
from .models import ItemReserva

class ItemReservaForm(forms.ModelForm):
    class Meta:
        model = ItemReserva
        fields = ['reserva', 'servico_adicional', 'quantidade']