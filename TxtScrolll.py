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

        #Creates a rectangle to be used as the border, since it is earlier in the draw list the next obj drawn will be "on top" giving the illusion of a border.
        #This should be functionalised to allow it to be altered programmtically when the text area class is made.
        borderX = self.x 
        borderY = self.y 
        self.batch.add(4, GL_QUADS, None, ("v2f", (borderX - 10, borderY - 10,  borderX + 10 + self.width, borderY - 10,  borderX + 10 + self.width, borderY + 10 + self.height,  borderX - 10, borderY + 10  + self.height,)), 
        ('c3B', (0, 255, 255, 0, 255, 255,0, 255, 255,0, 255, 255,)))

        #Creates a quad at 0,0,0 (the first vertex is at this location) with input variables.
        self.batch.add(4, GL_QUADS, None, ("v2f", (self.x, self.y,  self.x + self.width, self.y,  self.x + self.width, self.y + self.height,  self.x, self.y + self.height,)), 
        ('c3B', (255, 255, 255,255, 255, 255,255, 255, 255,255, 255, 255,)))

        self.addBlocks(self.x, self.y, self.width, self.height)

    #Fills the text area with blocks. StartX & startyY refer to the position of where blocks are started to be drawn from.
    def addBlocks(self, startX, startY, maxX, maxY):
        offsetX = 0
        offsetY = 0
        
        padding = 2
        startX = startX + padding
        startY = startY + padding

        #Workout how many blocks can be added on each row.
        rowBlockMax = maxX / 25
        colBlockMax = maxY / 25
        r = 0
        c = 0
        
        while c < colBlockMax:
            while r < rowBlockMax:
                self.blockList.append(Block(startX + offsetX, startY + offsetY))
                r += 1
                offsetX = offsetX + padding + 20
            r = 0
            offsetX = 0
            c += 1
            offsetY = offsetY + padding + 20
        return True


    def draw(self):
        self.batch.draw()
        self.drawBlocks()
    
    #Iterates through the blockList calling draw on each block, weather anything is output depends on that blocks flipped state.
    def drawBlocks(self):
        for i, val in enumerate(self.blockList):
            val.draw()


#The block class will be used to create letters.
class Block:
    def __init__(self, xPos, yPos):
        self.x = xPos
        self.y = yPos
        self.state = 0
        self.blockBatch = pyglet.graphics.Batch()
        self.blockSize = 20
        self.blockBatch.add(4, GL_QUADS, None, ("v2f", (self.x, self.y,   self.x + self.blockSize, self.y,   self.x + self.blockSize, self.y + self.blockSize,   self.x, self.y + self.blockSize,)),
        ("c3B", (255,0,0, 255,0,0, 255,0,0, 255,0,0,)))
    
    #Switches the block on or off.
    def flip(self):
        self.state = ~self.state
        return self.state
    
    def draw(self):
        #This adds the other part to the functionality of the blocks, allowing them to be "flipped" on or off.
        if(self.state == 0):
            self.blockBatch.draw()
        
        


#Window class for the application. Handles some basic input.
class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_minimum_size(400, 400)
        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)

        #Creates a text area with these values, for the time being the values entered should adhere to a plan for the size of the blocks, however in the future it would be better if the size of the textArea defined the size of the blocks.
        self.textArea = TextArea(50, 50, 600, 200)
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