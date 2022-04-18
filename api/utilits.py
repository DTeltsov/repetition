import os


def get_path(instance, filename):
    return os.path.join(
      "user_%d" % instance.owner.id, filename)


def get_song_path(instance, filename):
    return os.path.join("%d" % filename)