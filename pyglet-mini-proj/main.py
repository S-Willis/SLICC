import pyglet
from pyglet.window import key
import config
from system.component import Component
from entities.car import Car
from random import randint

window = pyglet.window.Window(height = config.window_height, width = config.window_width)

car = Car(x=0,y=0,speed = 2)

def draw():
    window.clear()
    car.draw_self()
    # if isinstance(car,Component):
    #     Car.draw_self()

def update(time):
    if isinstance(car,Component):
        car.update_self()


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.LEFT:
        print('Left Key!')
        if(car.x_direction == 1):
            car.x_direction *= -1
    elif symbol == key.RIGHT:
        print('Right key!')
        if(car.x_direction == -1):
            car.x_direction *= -1
    elif symbol == key.DOWN:
        print('Down key!')
        if(car.y_direction == 1):
            car.y_direction *= -1
    elif symbol == key.UP:
        print('Up key!')
        if(car.y_direction == -1):
            car.y_direction *= -1
    else:
        return

def main():

    @window.event
    def on_draw():
        draw()

    pyglet.clock.schedule_interval(update, 1/60.0)
    pyglet.app.run()


if __name__ == "__main__":
    main()
