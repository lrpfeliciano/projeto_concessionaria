from django.forms import ModelForm
from .models import Cliente, Marca

class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

