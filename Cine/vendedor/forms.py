from django import forms
from .models import Compra

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['funcion', 'entradas_mayores', 'entradas_menores',]