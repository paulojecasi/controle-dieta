# Generated by Django 3.1.2 on 2020-10-14 20:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dieta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refeicao', models.CharField(blank=True, choices=[('CAFE DA MANHA', 'CAFE DA MANHA'), ('LANCHE       ', 'LANCHE       '), ('ALMOÇO       ', 'ALMOÇO       '), ('JANTAR       ', 'JANTAR       '), ('CEIA         ', 'CEIA         ')], max_length=30, null=True, verbose_name='Refeição')),
                ('horario', models.TimeField(verbose_name='Horario')),
                ('descricao', models.CharField(blank=True, max_length=300, null=True, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Dados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_inicio', models.DateField(auto_now=True, null=True, verbose_name='Data Inicial')),
                ('dt_final', models.DateField(auto_now=True, null=True, verbose_name='Data Final')),
                ('peso', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Peso')),
                ('altura', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Altura')),
                ('peso_ideal', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Peso Ideal')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
    ]