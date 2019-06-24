import pyglet

pyglet.resource.path = ["C:\\Users\\skyli\\Documents\\Uni\\SLICC\\SLICC\\final-project\\Racing-Game\\resources\\"]
pyglet.resource.reindex()

car_image = pyglet.resource.image("car.png")

def sprite_center(image):
    image.anchor_x = image.width
    image.anchor_y = image.height/2

sprite_center(car_image)
