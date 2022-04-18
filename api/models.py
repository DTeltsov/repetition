from django.db import models
from django.contrib.auth.models import User
from .utilits import get_path, get_song_path


class Album(models.Model):
    title = models.CharField(max_length=250)
    number_of_songs = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.title


class Gener(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=250)
    albums = models.ManyToManyField(Album)
    geners = models.ManyToManyField(Gener, blank=True)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to=get_song_path)
    file = models.FileField(upload_to=get_song_path)
    duration = models.IntegerField(editable=False, default=0)
    song_number = models.SmallIntegerField(blank=True, null=True)
    artist = models.ManyToManyField(Artist, blank=True)
    album = models.ManyToManyField(Album, blank=True)
    genre = models.ManyToManyField(Gener, blank=True)
    year = models.CharField(max_length=4, blank=True)
    play_count = models.IntegerField(default=0)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    avatar = models.ImageField(upload_to=get_path, null=True, blank=True)
    songs = models.ManyToManyField(Song, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_username(self):
        return self.user.username
