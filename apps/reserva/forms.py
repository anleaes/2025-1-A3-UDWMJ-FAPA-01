from django import forms
from .models import Reserva
from imovel.models import Imovel 
from django.core.exceptions import ValidationError
from datetime import date

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = [
            'hospede',
            'imovel',
            'data_checkin',
            'data_checkout',
            'qtd_hospedes',
            'status',
        ]
        widgets = {
            'data_checkin': forms.DateInput(attrs={'type': 'date'}),
            'data_checkout': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self): # validação de um formulário
        cleaned_data = super().clean()
        data_checkin = cleaned_data.get('data_checkin')
        data_checkout = cleaned_data.get('data_checkout')
        imovel = cleaned_data.get('imovel')
        qtd_hospedes = cleaned_data.get('qtd_hospedes')
        status_atual = cleaned_data.get('status')

        # Data de Check-out deve ser posterior à Data de Check-in
        if data_checkin and data_checkout:
            if data_checkout <= data_checkin:
                raise ValidationError(
                    "A data de check-out deve ser posterior à data de check-in."
                )
            
            # Data de Check-in não pode ser no passado (apenas para novas reservas)
            if not self.instance.pk and data_checkin < date.today():
                 raise ValidationError(
                    "A data de check-in não pode ser no passado para uma nova reserva."
                )

        # Quantidade de Hóspedes não pode exceder o máximo do imóvel
        if imovel and qtd_hospedes:
            if qtd_hospedes > imovel.max_hospedes: 
                raise ValidationError(
                    {'qtd_hospedes': f"O número de hóspedes ({qtd_hospedes}) excede o máximo permitido pelo imóvel ({imovel.max_hospedes})."}
                )

        #  Disponibilidade do Imóvel
        if imovel and data_checkin and data_checkout:
            if status_atual in ['solicitada', 'confirmada']:
                if not imovel.is_available(data_checkin, data_checkout, self.instance.pk): # Chamada ao is_available aqui
                    raise ValidationError(
                        "O imóvel não está disponível para as datas selecionadas. Há outra reserva conflitante."
                    )
        
        return cleaned_data