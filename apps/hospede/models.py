from django.db import models

class Hospede(models.Model):
    name = models.CharField('Nome', max_length=50)
    email = models.EmailField('Email', max_length=100)
    password = models.CharField ('Senha', max_length=50)
    telephone = models.CharField('Telefone', max_length=13)
    
    
    class Meta:
        verbose_name = 'Hospede'
        verbose_name_plural = 'Hospedes'
        ordering =['id']

    def __str__(self):
        return self.name

