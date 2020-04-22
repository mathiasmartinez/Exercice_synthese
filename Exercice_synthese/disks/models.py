from django.db import models

# Create your models here.
class Track(models.Model):

    id = models.IntegerField()
    Name = models.CharField(max_length=100)
    Composer = models.CharField(max_length=100)
    Milliseconds = models.IntegerField()
    Bytes = models.IntegerField()
    Album = models.ForeignKey('album',on_delete=CASCADE)

    self


