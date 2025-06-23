from django.urls import path
from . import views

app_name = 'myAppurl'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('track/', views.track, name = 'track'),
    path('details/', views.details, name = 'details'),
    path('testimony/', views.testimony, name = 'testimony'),
    path('error/', views.error, name = 'error'),
    path('contact/', views.contact, name = 'contact'),





   
]