from django.http import HttpResponse
from .models import Album,Track,Artist
from django.shortcuts import render, redirect
from .forms import AlbumForm


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


    form = AlbumForm(request.POST or None)

    if form.is_valid():

        text = form.cleaned_data["Title"]
        A=False
        T=False
        albums = Album.objects.filter(Title__contains=text)
        tracks = Track.objects.filter(Name__contains=text)

        if len(albums)==0:
            A=True
        if len(tracks)==0:
            T=True
        return render(request, 'disks/resultat.html', locals())



    return render(request, 'disks/chercher.html', locals())




