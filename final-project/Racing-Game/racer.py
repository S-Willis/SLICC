import pyglet
from game import car

game_window = pyglet.window.Window(800,600)
pyglet.gl.glClearColor(0.5,0.5,0.7,0)

main_batch = pyglet.graphics.Batch()

lap_counter = pyglet.text.Label(text = "Lap: 0", x=10, y=575, batch=main_batch)
iteration_counter = pyglet.text.Label(text = "Iteration: 0", x = 700, y=575,batch=main_batch)

player_car = car.Car(x=400,y=300,batch=main_batch)

game_window.push_handlers(player_car.key_handler)


def update(dt):
    player_car.update(dt)


@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()

if __name__ == '__main__':

    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()
