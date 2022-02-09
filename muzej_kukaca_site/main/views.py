from django.shortcuts import render
from django.views.generic import ListView
from main.models import Korisnik, Kukac

class KorisnikList(ListView):
    model = Korisnik

class KukacList(ListView):
    model = Kukac

def homepage(request):
    return render(request, './homepage.html')

