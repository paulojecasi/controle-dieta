# Generated by Django 3.1.2 on 2020-10-14 20:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_dieta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dieta',
            name='dados',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dieta', to='app_dieta.dados'),
        ),
        migrations.AlterField(
            model_name='dados',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dados', to=settings.AUTH_USER_MODEL),
        ),
    ]