from django.db import models
from reserva.models import Reserva 

class Avaliacao(models.Model):
    
    reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE, related_name='avaliacao')
    nota = models.IntegerField('Nota', choices=[(i, str(i)) for i in range(1, 6)])
    comentario = models.TextField('Comentário', blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'

    def __str__(self):
        return f"Avaliação da Reserva {self.reserva.id} - Nota: {self.nota}"