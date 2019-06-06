import pyglet
from system.component import Component
import config

class Car(Component):

    def __init__(self, *args, **kwargs):

        super(Car, self).__init__(*args, **kwargs)
        self.speed = kwargs.get('speed', 2)##set default speed?
        self.car_image = pyglet.image.load('assets\\car.png')#set car_image
        self.width = self.car_image.width
        self.height = self.car_image.height
        self.car_sprite = pyglet.sprite.Sprite(self.car_image,self.x,self.y)
        self.x_direction = 1 #set direction?
        self.y_direction = 1

    def update_self(self):

        self.x += (self.speed * self.x_direction)
        self.y += (self.speed * self.y_direction)
        self.car_sprite.set_position(self.x,self.y)

        if(self.x < 0 or (self.x + self.width) > config.window_width):
            self.x_direction *= -1

        if(self.y < 0 or (self.y + self.width) > config.window_height):
            self.y_direction *= -1


    def draw_self(self):
        self.car_sprite.draw()
