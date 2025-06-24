from django.db import models
from reserva.models import Reserva 
from servico_adicional.models import ServicoAdicional 

class ItemReserva(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name='itens_reserva')
    servico_adicional = models.ForeignKey(ServicoAdicional, on_delete=models.CASCADE)
    quantidade = models.IntegerField('Quantidade', default=1)
    preco_unitario_na_reserva = models.DecimalField('Preço Unitário na Reserva', max_digits=8, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = 'Item da Reserva'
        verbose_name_plural = 'Itens da Reserva'
        
    def __str__(self):
        return f"Reserva {self.reserva.id} - {self.servico_adicional.nome} ({self.quantidade}x)"

    def calcular_subtotal(self) -> float:
        return self.quantidade * self.preco_unitario_na_reserva

    def save(self, *args, **kwargs): # Serve para o valor do serviço caso seja alterado nao altere na reserva
        if not self.pk and not self.preco_unitario_na_reserva:
            self.preco_unitario_na_reserva = self.servico_adicional.preco
        
        super().save(*args, **kwargs)
        
        self.reserva.calcular_preco_total()
        self.reserva.save(update_fields=['preco_total', 'atualizado_em'])

    def delete(self, *args, **kwargs):
        reserva_pai = self.reserva
        super().delete(*args, **kwargs) # Chama o método delete() original
        reserva_pai.calcular_preco_total()
        reserva_pai.save(update_fields=['preco_total', 'atualizado_em'])