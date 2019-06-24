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
        self.acceleration = 200.0
        self.rotate_speed = 400.0
        self.keys = dict(left=False, right=False, up=False)
        self.key_handler = key.KeyStateHandler()

    def update(self, dt):
        self.x += self.x_velocity * dt
        self.y += self.y_velocity * dt
        self.check_bounds()

        if self.key_handler[key.LEFT]:
            self.rotation -= self.rotate_speed *dt
        
        elif self.key_handler[key.RIGHT]:
            self.rotation += self.rotate_speed * dt

        if self.key_handler[key.UP]:
            angle_radians = -math.radians(self.rotation)
            x_force = math.cos(angle_radians) * self.acceleration
            y_force = math.sin(angle_radians) * self.acceleration
            self.x_velocity = x_force
            self.y_velocity = y_force
        else:
            self.x_velocity *= 0.9
            self.y_velocity *= 0.9

    def check_bounds(self):
        min_x = -self.image.width /2
        min_y = -self.image.width /2
        max_x = 800 + self.image.width/2
        max_y = 600 + self.image.height/2

        if self.x < min_x:
            self.x = max_x
        elif self.x > max_x:
            self.x = min_x

        if self.y < min_y:
            self.y = max_y
        elif self.y > max_y:
            self.y = min_y
