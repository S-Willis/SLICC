import pyglet
from system.component import Component
import config

class Ball(Component):

    def __init__(self, *args, **kwargs):
        super(Ball, self).__init__(*args,**kwargs)
        self.speed = kwargs.get('speed', 5)
        self.ball_image = pyglet.image.load()
        self.width = self.ball_image.width
        self.height = self.ball_image.height
        self.ball_sprite = pyglet.sprite.Sprite(self.ball_image,self.x,self.y)
        self.x_direction = 1
        self.y_direction = 1

        print("Ball Created!")

    def update_self(self):

        self.x += (self.speed * self.x_direction)
        self.y += (self.speed * self.y_direction)
        self.ball_sprite.set_position(self.x,self.y)

        if(self.x < 0 or (self.x + self.width) > config.window_width):
            self.x_direction *= -1

        if(self.y < 0 or (self.y + self.width) > config.window_height):
            self.y_direction *= -1

    def draw_self(self):
        self.ball_sprite.draw()
