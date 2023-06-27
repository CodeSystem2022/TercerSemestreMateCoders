from django import forms
from .models import Compra
from .models import Usuario

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['funcion', 'entradas_mayores', 'entradas_menores',]
        
        

class RegistroForm(forms.ModelForm):
    contraseña = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Usuario
        fields = ['nombre', 'correo', 'contraseña']
