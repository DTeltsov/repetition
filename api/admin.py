from django.contrib import admin
from .models import Album, Artist, Song, Profile, Gener

admin.site.register([Album, Artist, Song, Profile, Gener])

