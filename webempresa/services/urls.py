from django.urls import path
from .import views

urlpatterns = [

    #Paths del Services
    path('', views.services, name='services'),
   

]