import pyglet
import math
from pyglet.window import key
from . import resources, track
from PIL import Image

class Car(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super().__init__(img=resources.car_image,*args,**kwargs)
        self.x_velocity = 0.0
        self.y_velocity = 0.0
        self.dead = False
        self.acceleration = 150.0
        self.rotate_speed = 200.0
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

        self.collisions()

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

    def collisions(self):

        file = Image.open('C:\\Users\\skyli\\Documents\\Uni\\SLICC\\SLICC\\final-project\\Racing-Game\\resources\\collision_map.png')
        map = file.load()

        for x in range(int(self.x)-(int(self.width)//2),int(self.x)+(int(self.width)//2)):
            for y in range(int(self.y)-(int(self.height)//2),int(self.y)+(int(self.height)//2)):
                if map[x,y][0] != 0 :
                    self.dead = True
                else:
                    self.dead = False

        # collision_map = pyglet.image.load('C:\\Users\\skyli\\Documents\\Uni\\SLICC\\SLICC\\final-project\\Racing-Game\\resources\\collision_map.png')
        # imgData = collision_map.get_image_data()
        # region = imgData.get_region(self.x, self.y, self.width,self.height)
        # rgbData = region.get_data('RGB',300)
        # rgbList = rgbData.split('\\')
        #
        # for idx, val in enumerate(rgbList):
        #     if idx % 3 == 1 and val == 'xff':
        #         self.dead == True
        #     else:
        #         continue
