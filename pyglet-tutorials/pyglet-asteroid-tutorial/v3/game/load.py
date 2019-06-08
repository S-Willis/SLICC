import pyglet
import random
from . import resources, physicalobject
import math

asteroid_list = []

def distance(p1 = (0,0), p2 = (0,0)):
    return math.sqrt((p1[0] -p2[0])**2 + (p1[1] - p2[1])**2)

def player_lives(num_icons, batch=None):
    player_lives = []
    for icon in range(num_icons):
        new_sprite = pyglet.sprite.Sprite(img=resources.player_image,
                                          x=784-icon*30,
                                          y=585,
                                          batch = batch)
        new_sprite.scale = 0.5
        player_lives.append(new_sprite)
    return player_lives

def asteroids(num_asteroids, player_position, batch=None):

    for asteroid in range(num_asteroids):

        asteorid_x, asteroid_y = player_position

        while(distance((asteorid_x,asteroid_y), player_position) < 100):
            asteroid_x = random.randint(0,800)
            asteroid_y = random.randint(0,600)
        new_asteroid = physicalobject.PhysicalObject(img=resources.asteroid_image,
                                            x=asteroid_x, y=asteroid_y,
                                            batch = batch)
        new_asteroid.rotation = random.randint(0,360)
        new_asteroid.velocity_x = random.random()*40
        new_asteroid.velocity_y = random.random()*40
        asteroid_list.append(new_asteroid)

    return asteroid_list
