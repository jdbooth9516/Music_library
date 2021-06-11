from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=50, null=False)
    artist = models.CharField(max_length=50, null=False)
    album = models.CharField(max_length=50, null=False)
    release_date = models.DateTimeField()
    likes = models.IntegerField(default=0)

    