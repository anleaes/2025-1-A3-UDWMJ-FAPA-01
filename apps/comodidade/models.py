from django.db import models

class Comodidade(models.Model):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição', blank=True, null=True)

    class Meta:
        verbose_name = 'Comodidade'
        verbose_name_plural = 'Comodidades'

    def __str__(self):
        return self.nome