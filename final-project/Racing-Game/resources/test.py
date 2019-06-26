import pyglet
import random
from PIL import Image

# file = Image.open('collision_map.png').convert('RGB')
# map = file.load()
# print(map[400,500])

i = pyglet.image.load('collision_map.png')
d = i.get_image_data()
c = d.get_region(400,500, 10, 10)
b = c.get_data('RGB', c.pitch)

for x in range(abs(c.pitch)):
    if x % 3 == 0 and b[x] != 0:
        print("red")
        break
    else:
        print("green")
