import pyglet
import random
from rules import Rules
from pyglet.gl import *

class Window(pyglet.window.Window):

    def __init__(self):
        super().__init__(600,600)
        super().set_caption('Elementary CA')
        # rulenumber = random.randint(0,255)
        self.rulenumber = 120
        self.rules = Rules(self.get_size()[0], # grid width
                           self.get_size()[1], # grid height
                           7,  # size of each cell
                           self.rulenumber) # rulenumber
        pyglet.clock.schedule_interval(self.update, 1) # 24 fps

    def on_draw(self):
        self.clear()
        self.rules.draw()

    def update(self, dt):
        if self.rulenumber < 255:
            self.rulenumber += 1
        else:
            self.rulenumber = 1
        # rulenumber = random.randint(0,255)
        self.rules.generate_ca()
        self.rules = Rules(self.get_size()[0], # grid width
                           self.get_size()[1], # grid height
                           7,  # size of each cell
                           self.rulenumber) # rulenumber

if __name__ == '__main__': # creates instance of class
    window = Window()
    pyglet.app.run()
