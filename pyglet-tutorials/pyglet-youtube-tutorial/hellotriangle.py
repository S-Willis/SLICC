from pyglet.gl import *


class Triangle:

    def __init__(self):
        self.vertices = pyglet.graphics.vertex_list(3,('v3f',[-0.5,-0.5,0.0, 0.5,-0.5,0.0,0.0,0.5,0.0]), ('c3B', (0,200,0,200,0,0,0,0,200)))

class Quad:

    def __init__(self):
        self.vertices = pyglet.graphics.vertex_list_indexed(4, [0,1,2,2,3,0],
        ('v3f',[-0.5,-0.5,0.0, 0.5,-0.5,0.0,0.5,0.5,0.0,-0.5,0.5,0.0]),
        ('c3f',[1.0,0.0,0.0,1.0,0.0,0.0,1.0,0.0,0.0,1.0,0.0,0.0]))

class Quad2:

    def __init__(self):
        self.indeces = [0,1,2,2,3,0]
        self.vertex = [-0.5,-0.5,0.0, 0.5,-0.5,0.0,0.5,0.5,0.0,-0.5,0.5,0.0]
        self.colour = [1.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0]
        self.vertices = pyglet.graphics.vertex_list_indexed(4, (self.indeces),('v3f',self.vertex),('c3f',self.colour))


class Quad3:

    def __init__(self):
        self.indeces = [0,1,2,2,3,0]
        self.vertex = [-0.5,-0.5,0.0, 0.5,-0.5,0.0,0.5,0.5,0.0,-0.5,0.5,0.0]
        self.colour = [1.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0]

    def render(self):
        self.vertices = pyglet.graphics.draw_indexed(4, GL_TRIANGLES,(self.indeces),('v3f',self.vertex),('c3f',self.colour))



class MyWindow(pyglet.window.Window):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.set_minimum_size(400,300)
        glClearColor(0.2, 0.3,0.2,1.0)
        self.triangle = Triangle()
        self.quad3 = Quad3()

    def on_draw(self):
        self.clear()
        # self.triangle.vertices.draw(GL_TRIANGLES)
        # self.quad2.vertices.draw(GL_TRIANGLES)
        self.quad3.render()

    def on_resize(self,width,height):
        glViewport(0,0,width,height)


if __name__ == "__main__":
    window = MyWindow(720,360, "My Pyglet Window", resizable = True)
    # window.on_draw()
    pyglet.app.run()
