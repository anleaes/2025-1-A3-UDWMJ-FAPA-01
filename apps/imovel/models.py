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


    def is_available(self, checkin_date: date, checkout_date: date, current_reserva_id=None) -> bool:
     
        if not self.disponivel: 
            return False

        from reserva.models import Reserva 

        conflicting_reservas = Reserva.objects.filter(
            imovel=self,
            status__in=['solicitada', 'confirmada'] 
        ).filter(
            data_checkin__lt=checkout_date,
            data_checkout__gt=checkin_date
        )

        if current_reserva_id:
            conflicting_reservas = conflicting_reservas.exclude(id=current_reserva_id)

        return not conflicting_reservas.exists()