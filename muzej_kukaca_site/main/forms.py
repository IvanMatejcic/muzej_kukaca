from django import forms
from main.models import Korisnik, Kukac
from django.forms import ModelForm

class KukacForm(forms.ModelForm):

    class Meta:
        model = Kukac
        fields = ['vrsta', 'slika']

class KorisnikForm(forms.ModelForm):

    class Meta:
        model = Korisnik
        fields = ['username', 'slika_profila']

class SingUpForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Korisnik
        fields = ['username', 'ime', 'prezime', 'email']