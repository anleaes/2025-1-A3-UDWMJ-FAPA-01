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
        num_noites = 0
        if self.data_checkin and self.data_checkout and self.imovel:
            num_noites = (self.data_checkout - self.data_checkin).days
            if num_noites <= 0:
                num_noites = 0

        preco_base_imovel = 0.00
        if self.imovel and self.imovel.preco_por_noite is not None:
            preco_base_imovel = num_noites * self.imovel.preco_por_noite

        total_servicos_adicionais = 0.00
        if self.pk:  # Só tenta acessar os itens se a reserva já tem ID
            total_servicos_adicionais = sum(
                item.calcular_subtotal() for item in self.itens_reserva.all() #Metodo calcular_subtotal vem de item_reservas.
            )

        self.preco_total = preco_base_imovel + total_servicos_adicionais
        return self.preco_total

    def cancelar(self) -> bool:
        if self.status not in ['cancelada', 'concluida']:
            self.status = 'cancelada'
            self.save(update_fields=['status', 'atualizado_em'])
            return True
        return False

    def save(self, *args, **kwargs): #argumentos
        super().save(*args, **kwargs)  #salva no banco de dados
        self.calcular_preco_total()   # acessa
        super().save(update_fields=['preco_total', 'atualizado_em'])  # salva Atualizando só o necessário