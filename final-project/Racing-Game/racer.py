import pyglet
from game import car, track

game_window = pyglet.window.Window(800,600)
pyglet.gl.glClearColor(0.5,0.5,0.7,0)

main_batch = pyglet.graphics.Batch()

lap = 0
iteration = 0

lap_counter = pyglet.text.Label(text = "Lap: " + str(lap), x=10, y=575, batch=main_batch, color=(0,0,0,255))
iteration_counter = pyglet.text.Label(text = "Iteration: " + str(iteration), x = 700, y=575,batch=main_batch,color=(0,0,0,255))
level_track = track.Track(x=400,y=300,batch=main_batch)
player_car = car.Car(x=400,y=500,batch=main_batch)

game_window.push_handlers(player_car.key_handler)


def update(dt):
    player_car.update(dt)
    if player_car.dead:
        player_car.delete()


@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()

if __name__ == '__main__':

    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()
