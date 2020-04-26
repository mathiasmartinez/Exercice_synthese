from django import forms

class recherche(forms.Form):
    champ = forms.CharField(max_length=200)

