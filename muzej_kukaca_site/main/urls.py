from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'main'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('kukacs/', views.KukacList.as_view()),
    path('kukac_list', views.display_kukac_images, name = 'kukac_list'),
    url(r'^create/$', views.KukacCreate, name="create"),
    path('kukacs/<int:pk>', views.KukacDetailView.as_view(), name = "kukac-detail"),
    path('kukacs/<int:pk>/edit', views.KukacUpdateView.as_view(), name= "edit"),
    path('kukacs/<int:pk>/delete', views.KukacDeleteView.as_view(), name = "delete" )
]