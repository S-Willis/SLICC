import pyglet

pyglet.resource.path = ["C:\\Users\\skyli\\Documents\\Uni\\SLICC\\SLICC\\final-project\\Racing-Game\\resources\\"]
pyglet.resource.reindex()

car_image = pyglet.resource.image("car.png")

def center_image(image):
    image.anchor_x = image.width/2
    image.anchor_y = image.height/2

center_image(car_image)
