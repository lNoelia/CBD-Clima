from django import forms
from .models import *

class SearchForm(forms.Form):
    keyword = forms.CharField(label="Buscar", widget=forms.TextInput(attrs={'placeholder': 'Escriba...',}))