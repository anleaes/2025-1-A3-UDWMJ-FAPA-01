from django.db import models

class ServicoAdicional(models.Model):
    nome = models.CharField('Nome do Serviço', max_length=100)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Serviço Adicional'
        verbose_name_plural = 'Serviços Adicionais'

    def __str__(self):
        return f"{self.nome} (R$ {self.preco:.2f})"