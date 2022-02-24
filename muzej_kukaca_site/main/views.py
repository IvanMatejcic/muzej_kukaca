from . import forms
from .models import Kukac
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class KukacList(ListView):
    model = Kukac

class KukacDetailView(DetailView):
    context_object_name = 'obj'
    model = Kukac

class KukacCreateView(LoginRequiredMixin, CreateView):
    model = Kukac
    fields = '__all__'
    template_name = 'main/kukac_new.html'
    success_url = '/kukacs'
    login_url = '/accounts/login/'


class KukacUpdateView(LoginRequiredMixin, UpdateView):
    model = Kukac
    fields = '__all__'
    success_url = '/kukacs'
    login_url = '/accounts/login/'


class KukacDeleteView(LoginRequiredMixin, DeleteView):
   model = Kukac
   success_url = '/kukacs'
   login_url = '/accounts/login/'


def homepage(request):
    return render(request, './homepage.html')

def display_kukac_images(request):
  
    if request.method == 'GET':
        Kukacs = Kukac.objects.all() 
        return render((request, './kukac_list.html',
                     {'kukac_list' : Kukacs}))



