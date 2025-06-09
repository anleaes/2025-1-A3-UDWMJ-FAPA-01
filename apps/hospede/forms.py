from django import forms
from .models import Hospede

class HospedeForm(forms.ModelForm):

    class Meta:
        model = Hospede
        exclude = ()