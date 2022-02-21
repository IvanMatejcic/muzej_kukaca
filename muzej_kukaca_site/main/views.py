from re import L
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic import UpdateView, DeleteView, DetailView
from .models import Kukac
from . import forms

class KukacList(ListView):
    model = Kukac

class KukacDetailView(DetailView):
    context_object_name = 'obj'
    model = Kukac

class KukacUpdateView(UpdateView):
    model = Kukac
    fields = '__all__'
    success_url = '/kukacs'

class KukacDeleteView(DeleteView):
   model = Kukac
   success_url = '/kukacs/'

def homepage(request):
    return render(request, './homepage.html')

def display_kukac_images(request):
  
    if request.method == 'GET':
        Kukacs = Kukac.objects.all() 
        return render((request, './kukac_list.html',
                     {'kukac_list' : Kukacs}))

def KukacCreate(request):
    if request.method == 'POST':
        form = forms.CreateKukac(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('/kukacs')
    else:
        form = forms.CreateKukac()
    return render(request, 'main/kukac_new.html', { 'form': form })



