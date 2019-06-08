from pyglet.gl import *

class MyWindow(pyglet.window.Window):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.set_minimum_size(400,300)
        glClearColor(0.5,0.5,1.0,0.0)

    def on_draw(self):
        self.clear()

    def on_resize(self, width, height):
        glViewport(0,0,width,height)


if __name__ == "__main__":
    window = MyWindow(720,480, "Window", resizable = True)
    pyglet.app.run()
