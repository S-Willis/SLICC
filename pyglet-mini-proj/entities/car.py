import pyglet
import math
from system.component import Component
import config
# from Math import *

class Car(Component):

    def __init__(self, *args, **kwargs):

        super(Car, self).__init__(*args, **kwargs)
        # self.speed = kwargs.get('speed', 2)##set default speed?
        self.car_image = pyglet.image.load('assets\\car.png')#set car_image
        self.width = self.car_image.width
        self.height = self.car_image.height
        self.car_sprite = pyglet.sprite.Sprite(self.car_image,self.x,self.y)
        self.thrust = 300.0
        self.rotate_speed = 200.0
        self.keys = dict(left = False, right = False, up = False)
        self.x_velocity = kwargs.get('x_velocity', 0.0)
        self.y_velocity = kwargs.get('y_velocity', 0.0)
        self.rotation = kwargs.get('rotation', 0.0)

    def update_self(self,time):

        super(Car, self).update_self(time)

        if self.keys['left']:
            self.rotation -= self.rotate_speed * time

        if self.keys['right']:
            self.rotation += self.rotate_speed * time

        if self.keys['up']:
            angle_radians = -math.radians(self.rotation)
            force_x = math.cos(angle_radians) * self.thrust * time
            force_y = math.sin(angle_radians) * self.thrust * time
            self.x_velocity += force_x
            self.y_velocity += force_y

        # self.x += (self.speed * self.x_direction)
        # self.y += (self.speed * self.y_direction)
        # self.car_sprite.set_position(self.x,self.y)
        #
        # if(self.x < 0 or (self.x + self.width) > config.window_width):
        #     self.x_direction *= -1
        #
        # if(self.y < 0 or (self.y + self.width) > config.window_height):
        #     self.y_direction *= -1


    def draw_self(self):
        self.car_sprite.draw()


    # @window.event
    # def on_key_press(self, symbol, modifiers):
    #
    #     if (symbol == key.UP):
    #         self.keys['up'] = True
    #     elif (symbol == key.LEFT):
    #         self.keys['left'] = True
    #     elif (symbol == key.RIGHT):
    #         self.keys['right'] = True
    #
    # @window.event
    # def on_key_release(self,symbol,modifiers):
    #
    #     if (symbol == key.UP):
    #         self.keys['up'] = False
    #     elif (symbol == key.LEFT):
    #         self.keys['left'] = False
    #     elif (symbol == key.RIGHT):
    #         self.keys['right'] = False
