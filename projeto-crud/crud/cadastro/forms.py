from django import forms
from .models import Registro, Conta

class RegistroForm(forms.ModelForm):    
    class Meta:
        model = Registro
        fields = ['price', 'description', 'category', 'account']


class ContaForm(forms.ModelForm):
    class Meta:
        model = Conta
        fields = '__all__'