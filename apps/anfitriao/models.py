from django.db import models

class Anfitriao(models.Model):
    name = models.CharField('Nome', max_length=50)
    email = models.EmailField('Email', max_length=100)
    senha = models.CharField ('Senha', max_length=50)
    telefone = models.CharField('Telefone', max_length=13)
    biography = models.TextField('Descricao', max_length=300) 
    
    class Meta:
        verbose_name = 'Anfitriao'
        verbose_name_plural = 'Anfitrioes'
        ordering =['id']

    def __str__(self):
        return self.name
