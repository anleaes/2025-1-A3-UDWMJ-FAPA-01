from django.db import models
from reserva.models import Reserva 
class Pagamento(models.Model):

    reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE, related_name='pagamento')
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2)
    data_pagamento = models.DateField('Data do Pagamento', auto_now_add=True)
    
    METODO_CHOICES = [
        ('cartao_credito', 'Cartão de Crédito'),
        ('pix', 'PIX'),
        ('boleto', 'Boleto'),
    ]
    metodo = models.CharField('Método', max_length=20, choices=METODO_CHOICES)
    
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('pago', 'Pago'),
        ('falhou', 'Falhou'),
    ]
    status = models.CharField('Status', max_length=10, choices=STATUS_CHOICES, default='pendente')

    def __str__(self):
        return f"Pagamento {self.pk} (Reserva {self.reserva.id}) - Valor: R${self.valor} - Status: {self.status}"

    def processarPagamento(self) -> bool:
       
        if self.valor > 0 and self.metodo != 'boleto':
            self.status = 'pago'
            self.save() 
            return True
        else:
            self.status = 'falhou'
            self.save()
            return False