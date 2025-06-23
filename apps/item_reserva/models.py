from django.db import models
from reserva.models import Reserva
from servico_adicional.models import ServicoAdicional

class ItemReserva(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    servico_adicional = models.ForeignKey(ServicoAdicional, on_delete=models.CASCADE)
    quantidade = models.IntegerField('Quantidade', default=1)

    class Meta:
        verbose_name = 'Item da Reserva'
        verbose_name_plural = 'Itens da Reserva'
        unique_together = ('reserva', 'servico_adicional')

    def __str__(self):
        return f"Reserva {self.reserva.id} - {self.servico_adicional.nome} ({self.quantidade}x)"