from django.http import HttpResponse
from .models import Album,Track,Artist
from django.shortcuts import render, redirect

from .forms import recherche

def Albums(request):
    albums = Album.objects.all()
    chemin = []
    for alb in albums:
        chemin+=["http://127.0.0.1:8000/accueil/" + str(alb.id) + "/"]

    return render(request,'disks/Albums.html',locals())

def album(request,ident):
    album = Album.objects.all().get(id=ident).Title
    tracks = Track.objects.all().filter(Album=ident)

    return render(request,'disks/album.html',locals())

def Recherche(request):
    adresse = "love/"
    search = False
    form = recherche(request.POST or None)
    form.save()
    if form.is_valid():

        champ = form.cleaned_data["champ"]
        search = True
        adresse = 'Wall/'
        albums = Album.objects.filter(Title__contains=champ)
        tracks = Track.objects.filter(Name__contains=champ)
        artists = Artist.objects.filter(Name__contains=champ)
        return render(request, 'disks/resultat.html', locals())



    return render(request, 'disks/chercher.html', locals())

def Resultat(request,champ):
    albums = Album.objects.filter(Title__contains=champ)
    tracks = Track.objects.filter(Name__contains=champ)
    artists = Artist.objects.filter(Name__contains=champ)
    return render(request,'disks/resultat.html',locals())


