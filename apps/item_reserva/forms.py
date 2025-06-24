from django import forms
from .models import ItemReserva

class ItemReservaForm(forms.ModelForm):
    class Meta:
        model = ItemReserva
        fields = ['servico_adicional', 'quantidade'] 
        widgets = {
            'servico_adicional': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
        }