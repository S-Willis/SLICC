import pyglet
import math
from pyglet.window import key
from . import resources


class Car(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super().__init__(img=resources.car_image,*args,**kwargs)
        self.x_velocity = 0.0
        self.y_velocity = 0.0
        self.dead = False
        self.acceleration = 300.0
        self.rotate_speed = 200.0
        self.keys = dict(left=False, right=False, up=False)
        self.key_handler = key.KeyStateHandler()

    def update(self, dt):
        self.x += self.x_velocity * dt
        self.y += self.y_velocity * dt
        #self.check_track

        if self.key_handler[key.LEFT]:
            self.rotation -= self.rotate_speed *dt
        elif self.key_handler[key.RIGHT]:
            self.rotation += self.rotate_speed * dt

        if self.key_handler[key.UP]:
            angle_radians = -math.radians(self.rotation)
            x_force = math
