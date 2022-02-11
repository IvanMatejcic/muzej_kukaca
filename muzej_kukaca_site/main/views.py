from django.shortcuts import redirect, render
from django.views.generic import ListView
from main.models import Korisnik, Kukac
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

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


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('homepage')

    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request, './registration/register.html', context)
