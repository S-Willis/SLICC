import pyglet

pyglet.resource.path = ["C:\\Users\\skyli\\Documents\\Uni\\SLICC\\SLICC\\pyglet-tutorials\\pyglet-asteroid-tutorial\\resources\\"]
pyglet.resource.reindex()

player_image = pyglet.resource.image("player.png")
bullet_image = pyglet.resource.image("bullet.png")
asteroid_image = pyglet.resource.image("asteroid.png")
# engine_image = pyglet.resource.image("flame.png")
#
# engine_image.anchor_x - engine_image.width * 1.5
# engine_image.anchor_y = engine_image.height / 2


def center_image(image):
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2

center_image(player_image)
center_image(bullet_image)
center_image(asteroid_image)
