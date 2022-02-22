from . import forms
from .models import Kukac
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

class KukacList(ListView):
    model = Kukac

class KukacDetailView(DetailView):
    context_object_name = 'obj'
    model = Kukac

class KukacCreateView(CreateView):
    form_class = forms.CreateKukac
    model = Kukac
    success_url = '/kukacs'

class KukacUpdateView(UpdateView):
    model = Kukac
    fields = '__all__'
    success_url = '/kukacs'

class KukacDeleteView(DeleteView):
   model = Kukac
   success_url = '/kukacs'

def homepage(request):
    return render(request, './homepage.html')

def display_kukac_images(request):
  
    if request.method == 'GET':
        Kukacs = Kukac.objects.all() 
        return render((request, './kukac_list.html',
                     {'kukac_list' : Kukacs}))



