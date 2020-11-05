import pyglet
from game import car, track

game_window = pyglet.window.Window(800,600)

main_batch = pyglet.graphics.Batch()
background = pyglet.graphics.OrderedGroup(0)
foreground = pyglet.graphics.OrderedGroup(1)

auto_x = 350
auto_y = 500

lap = 0
iteration = 0

lap_counter = pyglet.text.Label(text = "Lap: " + str(lap), x=10, y=575, batch=main_batch,
                                group=foreground,color=(0,0,0,255))
iteration_counter = pyglet.text.Label(text = "Iteration: " + str(iteration),
                                        x = 700, y=575,batch=main_batch,
                                        group=foreground,color=(0,0,0,255))

level_track = track.Track(x=400,y=300,batch=main_batch, group=background)
player_car = car.Car(x=auto_x,y=auto_y,batch=main_batch,group=foreground)
game_object = [player_car]

game_window.push_handlers(player_car.key_handler)


def update(dt):
    for obj in game_object:
        obj.update(dt)
        if obj.dead:
            global iteration
            iteration += 1
            iteration_counter.text = "Iteration: " + str(iteration)
            reset(obj)
        if obj.x == 380 and obj.y > 450:
            global lap
            lap += 1
            lap_counter.text = "Lap: " + str(lap)



def reset(obj):
    obj.dead = False
    obj.x = auto_x
    obj.y = auto_y
    obj.rotation = 0.0
    obj.x_velocity = 0.0
    obj.y_velocity = 0.0


@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()
