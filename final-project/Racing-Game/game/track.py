import pyglet
from . import resources

class Track(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(img = resources.track_image, *args, **kwargs)
