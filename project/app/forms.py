from django import forms

class formRepositorio(forms.Form):
    nome = forms.CharField(label='Nome do repositório:', max_length=100)
    linguagem = forms.CharField(label='Linguagem:', max_length=100)
