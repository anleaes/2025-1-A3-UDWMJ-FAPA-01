from django import forms
from .models import Anfitriao

class AnfitriaoForm(forms.ModelForm):

    class Meta:
        model = Anfitriao
        exclude = ()