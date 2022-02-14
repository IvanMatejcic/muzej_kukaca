from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('korisniks/', views.KorisnikList.as_view()),
    path('kukacs/', views.KukacList.as_view()),
    path('kukac_list', views.display_kukac_images, name = 'kukac_list'),
    path('korisnik_list', views.display_korisnik_images, name = 'korisnik_list'),
    path('new/', views.KukacCreateView.as_view()),
]