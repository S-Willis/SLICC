import pyglet
import random
from . import resources
import math

asteroid_list = []

def distance(p1 = (0,0), p2 = (0,0)):
    return math.sqrt((p1[0] -p2[0])**2 + (p1[1] - p2[1])**2)

def asteroids(num_asteroids, player_position):

    for asteroid in range(num_asteroids):

        asteorid_x, asteroid_y = player_position

        while(distance((asteorid_x,asteroid_y), player_position) < 100):
            asteroid_x = random.randint(0,800)
            asteroid_y = random.randint(0,600)
        new_asteroid = pyglet.sprite.Sprite(img=resources.asteroid_image,
                                            x=asteroid_x, y=asteroid_y)
        new_asteroid.rotation = random.randint(0,360)
        asteroid_list.append(new_asteroid)

    return asteroid_list
