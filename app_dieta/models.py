from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Dados(models.Model):

    user = models.ForeignKey(User, related_name='dados',
                                on_delete=models.CASCADE,
                                null=True)
    dt_inicio = models.DateField('Data Inicial', blank=True, null=True, auto_now=False)
    dt_final  = models.DateField('Data Final', blank=True, null=True, auto_now=False)
    peso = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Peso')
    altura = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Altura')
    peso_ideal = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Peso Ideal')



class Dieta(models.Model):
    REFEICAO = (
        ('CAFE DA MANHA', 'CAFE DA MANHA'),
        ('LANCHE       ', 'LANCHE       '),
        ('ALMOÇO       ', 'ALMOÇO       '),
        ('JANTAR       ', 'JANTAR       '),
        ('CEIA         ', 'CEIA         ')

    )

    dados= models.ForeignKey(Dados, related_name='dieta',
                                on_delete=models.CASCADE,
                                null=True)

    refeicao = models.CharField(max_length=30, verbose_name='Refeição',
                blank=True, null=True, choices=REFEICAO)
    horario = models.TimeField(auto_now=False, auto_now_add=False,
                                 verbose_name='Horario')
    descricao = models.CharField(max_length=300, blank=True, null=True,
                                 verbose_name='Descrição')

