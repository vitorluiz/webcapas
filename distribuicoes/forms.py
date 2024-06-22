# distribuicoes/forms.py

from django import forms

class DistribuicaoCSVForm(forms.Form):
    arquivo_csv = forms.FileField()
