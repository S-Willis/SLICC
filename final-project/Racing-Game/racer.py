import pyglet
from game import car, track

game_window = pyglet.window.Window(800,600)

main_batch = pyglet.graphics.Batch()
background = pyglet.graphics.OrderedGroup(0)
foreground = pyglet.graphics.OrderedGroup(1)

lap = 0
iteration = 0

lap_counter = pyglet.text.Label(text = "Lap: " + str(lap), x=10, y=575, batch=main_batch,
                                group=foreground,color=(0,0,0,255))
iteration_counter = pyglet.text.Label(text = "Iteration: " + str(iteration),
                                        x = 700, y=575,batch=main_batch,
                                        group=foreground,color=(0,0,0,255))
level_track = track.Track(x=400,y=300,batch=main_batch, group=background)
player_car = car.Car(x=400,y=500,batch=main_batch,group=foreground)
game_object = [player_car]

game_window.push_handlers(player_car.key_handler)


def update(dt):
    for obj in game_object:
        obj.update(dt)
        if obj.dead:
            obj.delete()
            game_object.remove(obj)
    if game_object == []:
        pyglet.app.exit()


@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()
