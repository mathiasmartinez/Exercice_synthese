from . import views
from django.urls import path
from . import models

urlpatterns = [
    path('', views.Albums),
    path('<int:ident>/', views.album, name='afficher_album'),
    path('recherche/', views.Recherche, name='chercher'),



]
