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

        self.blockList = []

        #Creates a quad at 0,0,0 (the first vertex is at this location) with input variables.
        self.batch.add(4, GL_QUADS, None, ("v2f", (self.x, self.y,  self.x + self.width, self.y,  self.x + self.width, self.y + self.height,  self.x, self.y + self.height,)), 
        ('c3B', (255, 255, 255,255, 255, 255,255, 255, 255,255, 255, 255,)))

        self.addBlocks()

    #Fills the text area with blocks.
    def addBlocks(self):
        self.blockList.append(Block(100, 100))
        self.drawBlocks()
        return True

    def draw(self):
        self.batch.draw()
    
    def drawBlocks(self):
        for i, val in enumerate(self.blockList):
            print(i, ",", val)

#The block class will be used to create letters.
class Block:
    def __init__(self, xPos, yPos):
        self.x = xPos
        self.y = yPos
        self.state = 0
        self.blockBatch = pyglet.graphics.Batch()
        self.blockSize = 25
        self.blockBatch.add(4, GL_QUADS, None, ("v2f", (self.x, self.y,   self.x + self.blockSize, self.y,   self.x + self.blockSize, self.y + self.blockSize,   self.x, self.y + self.blockSize,)),
        ("c3B", (0,0,0, 0,0,0, 0,0,0, 0,0,0,)))
    
    #Switches the block on or off.
    def flip():
        state = ~state
        return state
    
    def draw(self):
        self.blockBatch.draw()


#Window class for the application. Handles some basic input.
class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_minimum_size(400, 400)
        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)

        self.textArea = TextArea(105, 105, 500, 200)
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