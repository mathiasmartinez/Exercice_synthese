from django.db import models
from django import forms
# Create your models here.
class Track(models.Model):

    Name = models.CharField(max_length=160)
    id = models.IntegerField(primary_key=True)
    Composer = models.CharField(max_length=160)
    Milliseconds = models.IntegerField()
    Bytes = models.IntegerField()
    Album = models.ForeignKey('Album',on_delete=models.CASCADE)
    UnitPrice= models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return self.id

class Album(models.Model):
    id = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=160)
    Artist = models.ForeignKey('Artist',on_delete=models.CASCADE)

    def __str__(self):
        return self.id

class Artist(models.Model):

    id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=160)

    def __str__(self):
        return self.id


