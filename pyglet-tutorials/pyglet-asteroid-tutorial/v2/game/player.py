from . import physicalobject, resources
import math
from pyglet.window import key
from . import physicalobject, resources


class Player(physicalobject.PhysicalObject):

    def __init__(self, *args, **kwargs):
        super().__init__(img=resources.player_image, *args, **kwargs)
        self.thrust = 300.0
        self.rotate_speed = 200.0
        self.keys= dict(left=False, right=False, up=False)
        # self.key_handler = key.KeyStateHandler()

        # self.engine_sprite = pyglet.sprite.Sprite(img=resources.engine_image, *args, **kwargs)
        # self.engine_sprite.visible = False

    # @game_window.event
    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.keys['up'] = True
        elif symbol == key.RIGHT:
            self.keys['right'] = True
        elif symbol == key.LEFT:
            self.keys['left'] = True

    # @game_window.event
    def on_key_release(self,symbol,modifiers):
        if symbol == key.UP:
            self.keys['up'] = False
        elif symbol == key.RIGHT:
            self.keys['right'] = False
        elif symbol == key.LEFT:
            self.keys['left'] = False

    def update(self, dt):
        super(Player, self).update(dt)

        # if self.key_handler['left']:
        if self.keys['left']:
            self.rotation -= self.rotate_speed * dt
        # elif self.key_handler['right']:
        if self.keys['right']:
            self.rotation += self.rotate_speed * dt

        # if self.key_handler['up']:
        if self.keys['up']:
            angle_radians = -math.radians(self.rotation)
            force_x = math.cos(angle_radians) * self.thrust * dt
            force_y = math.sin(angle_radians) * self.thrust *dt
            self.velocity_x += force_x
            self.velocity_y += force_y
# DO KEY EVENT HANDLER
