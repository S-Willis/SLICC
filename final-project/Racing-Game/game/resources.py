import pyglet

pyglet.resource.path = ["C:\\Users\\skyli\\Documents\\Uni\\SLICC\\SLICC\\final-project\\Racing-Game\\resources\\"]
pyglet.resource.reindex()

car_image = pyglet.resource.image("car.png")
track_map = pyglet.resource.image("collision_map.png")
track_image = pyglet.resource.image("track.png")

def sprite_center(image):
    image.anchor_x = image.width/2
    image.anchor_y = image.height/2

sprite_center(car_image)
sprite_center(track_image)
sprite_center(track_map)

file = pyglet.image.load('C:\\Users\\skyli\\Documents\\Uni\\SLICC\\SLICC\\final-project\\Racing-Game\\resources\\collision_map.png')
map = file.get_image_data()
