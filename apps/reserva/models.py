from django.db import models
from hospede.models import Hospede
from imovel.models import Imovel
from datetime import date

class Reserva(models.Model):
    STATUS_CHOICES = (
        ('solicitada', 'Solicitada'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
        ('concluida', 'Concluída'),
    )

    hospede = models.ForeignKey(Hospede, on_delete=models.CASCADE, related_name='reservas')
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, related_name='reservas')
    data_checkin = models.DateField('Data de Check-in')
    data_checkout = models.DateField('Data de Check-out')
    qtd_hospedes = models.IntegerField('Quantidade de Hóspedes')
    preco_total = models.DecimalField('Preço Total', max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, default='solicitada')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering = ['-criado_em']

    def __str__(self):
        return f"Reserva {self.id} - {self.imovel.titulo} ({self.data_checkin} a {self.data_checkout})"

    def calcular_preco_total(self) -> float:

        if self.data_checkin and self.data_checkout and self.imovel and self.imovel.preco_por_noite is not None:
            num_noites = (self.data_checkout - self.data_checkin).days
            
            if num_noites > 0:
                self.preco_total = num_noites * self.imovel.preco_por_noite
            else:
                self.preco_total = 0.00 # Se checkin >= checkout, o valor é zero
        else:
            self.preco_total = 0.00 # Se faltar dados, o preço é zero

        return self.preco_total

    def cancelar(self) -> bool: 
       
        if self.status not in ['cancelada', 'concluida']:
            self.status = 'cancelada'
            self.save(update_fields=['status', 'atualizado_em'])
            return True
        return False