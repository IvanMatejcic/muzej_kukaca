from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('korisniks/', views.KorisnikList.as_view()),
    path('kukacs/', views.KukacList.as_view()),
]