from django.db import models
from comodidade.models import Comodidade
from imovel.models import Imovel

class ComodidadeImovel(models.Model):
    comodidade = models.ForeignKey(Comodidade, on_delete=models.CASCADE)
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Comodidade do Imóvel'
        verbose_name_plural = 'Comodidades do Imóvel'
        unique_together = ('comodidade', 'imovel') #para que nao seja associada ao mesmo imóvel mais de uma vez.

    def __str__(self):
        return f"{self.comodidade.nome} em {self.imovel.titulo}"