from django import forms
from .models import ServicoAdicional

class ServicoAdicionalForm(forms.ModelForm):
    class Meta:
        model = ServicoAdicional
        exclude = () 