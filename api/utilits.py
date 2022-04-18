import os


def get_path(instance, filename):
    return os.path.join('images', 'user_%d' % instance.user.id, filename)


def get_song_path(instance, filename):
    return os.path.join('songs', 'song_%d' % instance.id, filename)