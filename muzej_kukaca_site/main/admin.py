from django.contrib import admin
from .models import *

models_list = [Korisnik, Kukac]
admin.site.register(models_list)