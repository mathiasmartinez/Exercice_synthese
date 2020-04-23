from . import views
from django.urls import path

urlpatterns = [
    path('accueil/',views.Albums),
    path('accueil/<int:ident>/',views.album, name='afficher_album'),
    path('recherche/',views.Recherche)

]