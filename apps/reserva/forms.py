from django import forms
from django.forms import inlineformset_factory
from .models import Reserva
from imovel.models import Imovel
from item_reserva.models import ItemReserva 
from item_reserva.forms import ItemReservaForm 
from datetime import date
from django.core.exceptions import ValidationError

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

    # Método clean() serve para validar
    def clean(self):
        cleaned_data = super().clean()
        data_checkin = cleaned_data.get('data_checkin')
        data_checkout = cleaned_data.get('data_checkout')
        imovel = cleaned_data.get('imovel')
        qtd_hospedes = cleaned_data.get('qtd_hospedes')
        status_atual = cleaned_data.get('status')

        if data_checkin and data_checkout: #Se a data de check-out é maior que a de check-in.
            if data_checkout <= data_checkin:
                raise ValidationError(
                    "A data de check-out deve ser posterior à data de check-in."
                )
            
            if not self.instance.pk and data_checkin < date.today(): #Se a data de check-in para novas reservas não está no passado.
                 raise ValidationError(
                    "A data de check-in não pode ser no passado para uma nova reserva."
                )

        if imovel and qtd_hospedes: #Se a quantidade de hospedes não ultrapassa o limite do imóvel.
            if qtd_hospedes > imovel.max_hospedes:
                raise ValidationError(
                    {'qtd_hospedes': f"O número de hóspedes ({qtd_hospedes}) excede o máximo permitido pelo imóvel ({imovel.max_hospedes})."}
                )

        if imovel and data_checkin and data_checkout: #Se o imovel esta disponivel pois pode haver outra reserva conflitante.
            if status_atual in ['solicitada', 'confirmada']:
                current_reserva_id = self.instance.pk if self.instance else None
                if not imovel.is_available(data_checkin, data_checkout, current_reserva_id):
                    raise ValidationError(
                        "O imóvel não está disponível para as datas selecionadas. Há outra reserva conflitante."
                    )
        
        return cleaned_data


#Forms para fazer ligação com ItemReserva para a logica do carrinho
ItemReservaFormSet = inlineformset_factory(
    Reserva, 
    ItemReserva, 
    form=ItemReservaForm, 
    extra=1, 
    can_delete=True, 
    min_num=0, 
    validate_min=False, #permite que campo serviço nao precise de um item obrigatorio
)