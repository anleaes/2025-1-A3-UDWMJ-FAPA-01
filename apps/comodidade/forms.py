from django import forms
from .models import Comodidade

class ComodidadeForm(forms.ModelForm):
    class Meta:
        model = Comodidade
        exclude = () 