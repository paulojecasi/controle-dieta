from django.contrib import admin

# Register your models here.

from .models import Dados, Dieta

admin.site.register(Dados)
admin.site.register(Dieta)