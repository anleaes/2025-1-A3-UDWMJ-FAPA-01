from django.db import models
from anfitriao.models import Anfitriao
from datetime import date

class Imovel(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    endereco = models.TextField()
    preco_por_noite = models.DecimalField(max_digits=8, decimal_places=2)
    max_hospedes = models.IntegerField()
    quartos = models.IntegerField()
    banheiros = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    anfitriao = models.ForeignKey(Anfitriao, on_delete=models.CASCADE, related_name='imoveis')

    def __str__(self):
        return self.titulo


#Apos reserva estar implementado testar funcionamento dessa funcao

    # def is_available(self, checkin: date, checkout: date) -> bool:
    #     reservas_existentes = self.reserva_set.filter(
    #         status='confirmada',
    #         data_checkout__gt=checkin, #gt maior que
    #         data_checkin__lt=checkout #lt menor que
    #     )
    #     return not reservas_existentes.exists() 