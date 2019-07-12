#!/usr/bin/env python

import pyglet
import random
from pyglet.gl import *
from pyglet.window import *
import math

#Visible area to display the text against.
class TextArea:
    def __init__(self, xPos, yPos, taWidth, taHeight):
        self.width = taWidth
        self.height = taHeight
        self.x = xPos
        self.y = yPos
        self.batch = pyglet.graphics.Batch()

        #Creates a quad at 0,0,0 (the first vertex is at this location) with input variables.
        self.batch.add(4, GL_QUADS, None, ("v2f", (x, y,  x + width, y,  x + width, y + height,  x, y + height,)), 
        ('c3B', (255, 255, 255,255, 255, 255,255, 255, 255,255, 255, 255,)) )

    def draw(self):
        self.batch.draw()

#Window class for the application. Handles some basic input.
class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_minimum_size(400, 400)
        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)

        self.textArea = TextArea(100, 100, 500, 200)
        #pyglet.clock.schedule(self.update)


    'Handles key presses, two keybinds SPACE and ESC hard coded'
    def on_key_press(self,KEY,MOD):
        if KEY == key.ESCAPE: self.close()
        elif KEY == key.E: self.mouse_lock = not self.mouse_lock
    
    #delta time, how much time has passed.
    #def update(self,dt):
        #empty

    def on_draw(self):
        self.clear()
        self.textArea.draw()


if __name__ == '__main__':
    window = Window(width=700, height=700, caption="txtScrolll", resizable=True)
    glClearColor(0,0,0,1)
    pyglet.app.run()