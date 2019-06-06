import pyglet

window = pyglet.window.Window(height = 360, width = 480)

@window.event
def on_key_press(symbol, modifiers):
    print('A key was pressed: ' + str(symbol))
    # if symbol == key.LEFT:
    #     while(key.LEFT):
    #         print("LEFT!")


pyglet.app.run()
