import pyglet
import random
from . import resources, physicalobject, util, asteroid
import math

asteroid_list = []

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

    for i in range(num_asteroids):

        asteorid_x, asteroid_y = player_position

        while(util.distance((asteorid_x,asteroid_y), player_position) < 100):
            asteroid_x = random.randint(0,800)
            asteroid_y = random.randint(0,600)
        new_asteroid = asteroid.Asteroid(x=asteroid_x, y=asteroid_y,batch = batch)
        new_asteroid.rotation = random.randint(0,360)
        new_asteroid.velocity_x = random.random()*40
        new_asteroid.velocity_y = random.random()*40
        asteroid_list.append(new_asteroid)

    return asteroid_list
