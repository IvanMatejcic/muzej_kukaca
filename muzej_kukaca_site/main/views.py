from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from .models import *
from unittest import result
from urllib import request

class KorisnikList(ListView):
    model = Korisnik

class KukacList(ListView):
    model = Kukac

def homepage(request):
    return render(request, './homepage.html')

def display_kukac_images(request):
  
    if request.method == 'GET':
        Kukacs = Kukac.objects.all() 
        return render((request, './kukac_list.html',
                     {'kukac_list' : Kukacs}))

def display_korisnik_images(request):
  
    if request.method == 'GET':
        Korisniks = Korisnik.objects.all() 
        return render((request, './korisnik_list.html',
                     {'korisnik_list' : Korisniks}))

class KukacCreateView(LoginRequiredMixin, CreateView):
    model = Kukac
    template_name = 'kukac_new.html'
    fields = ['vrsta', 'porodica', 'red', 'datum_sakupljanja', 'lokalitet', 'duljina', 'spol', 'dostupan', 'opis', 'lovac', 'slika']
    success_url = "/"