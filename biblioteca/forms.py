from django import forms
from .models import Escritor, Livro

class EscritorForm(forms.ModelForm):
    class Meta:
        model = Escritor
        fields = ['nome', 'email']
        widgets = {
            'nome': forms.TextInput(attrs={
                'placeholder': 'Digite o nome completo do escritor',
                'class': 'form-control',
                'style': 'background: white !important; color: black !important;',
                'autocomplete': 'off'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Digite o email do escritor',
                'class': 'form-control',
                'style': 'background: white !important; color: black !important;',
                'autocomplete': 'off'
            }),
        }

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'escritor', 'data_publicacao', 'isbn']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'placeholder': 'Digite o título do livro',
                'class': 'form-control',
                'style': 'background: white !important; color: black !important;',
                'autocomplete': 'off'
            }),
            'data_publicacao': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'style': 'background: white !important; color: black !important;'
            }),
            'isbn': forms.TextInput(attrs={
                'placeholder': 'Digite o ISBN (13 dígitos)',
                'class': 'form-control',
                'style': 'background: white !important; color: black !important;',
                'autocomplete': 'off'
            }),
            'escritor': forms.Select(attrs={
                'class': 'form-control',
                'style': 'background: white !important; color: black !important;'
            }),
        }