import pyglet
import config
from system.component import Component
from entities.ball import Ball
from random import randint

window = pyglet.window.Window(height = config.window_height, width = config.window_width)

ball_objects = []

def draw():
    window.clear()
    for ball in ball_objects:
        if isinstance(ball,Component):
            ball.draw_self()

def update(time):
    for ball in ball_objects:
        if isinstance(ball,Component):
            ball.update_self()

@window.event
def on_mouse_press(x,y,button,modifiers):

    print('x: {}, y: {}'.format(x, y))
    ball_objects.append(Ball(x=x,y=y, speed=randint(3,12)))

def main():

    @window.event
    def on_draw():
        draw()

    pyglet.clock.schedule_interval(update, 1/60.0)
    pyglet.app.run()

main()
