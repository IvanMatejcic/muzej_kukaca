from django import forms
from main.models import Korisnik, Kukac

class KukacForm(forms.ModelForm):

    class Meta:
        model = Kukac
        fields = ['vrsta', 'slika']

class KorisnikForm(forms.ModelForm):

    class Meta:
        model = Korisnik
        fields = ['username', 'slika_profila']