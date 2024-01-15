
from .views import *
from django.urls import path

urlpatterns = [
    path("suscrito/<email>", suscrito),
    path("suscribir/<email>", suscribir),
   
]
