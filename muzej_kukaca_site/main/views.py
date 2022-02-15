from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from .models import Korisnik, Kukac
from unittest import result
from urllib import request
from . import forms


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

def KukacCreate(request):
    if request.method == 'POST':
        form = forms.CreateKukac(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            #instance.lovac = request.user
            instance.save()
            return redirect('/kukacs')
    else:
        form = forms.CreateKukac()
    return render(request, 'main/kukac_new.html', { 'form': form })