from django.http import HttpResponse
from .models import Album,Track,Artist
from django.shortcuts import render

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