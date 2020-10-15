from django.forms import ModelForm
from .models import Dados, Dieta

class DadosForm(ModelForm):
    class Meta:
        model = Dados
        fields = '__all__'

