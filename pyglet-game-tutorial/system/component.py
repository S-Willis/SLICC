import abc

class Component(metaclass=abc.ABCMeta):

    def __init__(self,**kwargs):

        self.active = kwargs.get('active',True)
        self.render = kwargs.get('render',True)
        self.debug = kwargs.get('debug', False)
        self.x = kwargs.get('x',0.0)
        self.y = kwargs.get('y',0.0)
        self.width = kwargs.get('width', 0)
        self.height = kwargs.get('height',0)

    @abc.abstractmethod
    def update_self(self):
        pass

    @abc.abstractmethod
    def draw_self(self):
        pass
