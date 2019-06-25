import pyglet
import random
from PIL import Image

file = Image.open('collision_map.png')
map = file.load()
print(map[0,0])
