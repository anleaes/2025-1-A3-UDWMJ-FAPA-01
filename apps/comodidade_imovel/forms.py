from django import forms
from .models import ComodidadeImovel

class ComodidadeImovelForm(forms.ModelForm):
    class Meta:
        model = ComodidadeImovel
        fields = ['comodidade', 'imovel']