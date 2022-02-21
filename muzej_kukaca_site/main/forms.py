from django import forms
from main.models import Kukac
from django.forms import ModelForm

class KukacForm(forms.ModelForm):
    class Meta:
        model = Kukac
        fields = ['vrsta', 'slika']

class CreateKukac(forms.ModelForm):
    class Meta:
        model = Kukac
        fields = '__all__'