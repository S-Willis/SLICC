import pyglet
from pyglet.window import key
import config
from system.component import Component
from entities.car import Car
from random import randint

time = 1/60.0

window = pyglet.window.Window(height = config.window_height, width = config.window_width)

car = Car(x=config.window_width/2,y=config.window_height/2,speed = 0)

def draw():
    window.clear()
    car.draw_self()
    # if isinstance(car,Component):
    #     Car.draw_self()

def update(time):
    if isinstance(car,Component):
        car.update_self(time)


# @window.event
# def on_key_press(symbol, modifiers):
#     if symbol == key.LEFT:
#         print('Left Key!')
#         if(car.x_direction == 1):
#             car.x_direction *= -1
#     elif symbol == key.RIGHT:
#         print('Right key!')
#         if(car.x_direction == -1):
#             car.x_direction *= -1
#     elif symbol == key.DOWN:
#         print('Down key!')
#         if(car.y_direction == 1):
#             car.y_direction *= -1
#     elif symbol == key.UP:
#         print('Up key!')
#         if(car.y_direction == -1):
#             car.y_direction *= -1
#     else:
#         return


@window.event
def on_key_press(symbol, modifiers):

    if (symbol == key.UP):
        car.keys['up'] = True
    elif (symbol == key.LEFT):
        car.keys['left'] = True
    elif (symbol == key.RIGHT):
        car.keys['right'] = True

@window.event
def on_key_release(symbol,modifiers):

    if (symbol == key.UP):
        car.keys['up'] = False
    elif (symbol == key.LEFT):
        car.keys['left'] = False
    elif (symbol == key.RIGHT):
        car.keys['right'] = False

def main():

    @window.event
    def on_draw():
        draw()

    pyglet.clock.schedule_interval(update, 1/60.0)
    pyglet.app.run()


if __name__ == "__main__":
    main()
