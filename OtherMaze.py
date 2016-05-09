import numpy as np
from Tkinter import *

import random

height = 41
width = 41
cell_size = 20 

maze = np.zeros((width, height))

class Player(object):
    def __init__(self, maze, canvas):
        self.maze = maze
        self.canvas = canvas
        self.x = 1
        self.y = 1
        self.id = None
        
    def moveup(self, event):
        if not self.maze[self.x, self.y - 1]:
            return False
        self.y -= 1
        self.canvas.move(self.id, 0, -cell_size)
    def movedown(self, event):
        if not self.maze[self.x, self.y + 1]:
            return False
        self.y += 1
        self.canvas.move(self.id, 0, cell_size)
    def moveleft(self, event):
        if not self.maze[self.x - 1, self.y]:
            return False
        self.x -= 1
        self.canvas.move(self.id, -cell_size, 0)
    def moveright(self, event):
        if not self.maze[self.x + 1, self.y]:
            return False
        self.x += 1
        self.canvas.move(self.id, cell_size, 0)
c = [(1,1)]

maze[c[0]] = 1

DIRS = [(0,1),(0,-1),(1,0),(-1,0)]

while c:
    ix = len(c) - 1
    x,y = c[ix]
    random.shuffle(DIRS)
    for dir in DIRS:
        dx,dy = dir
        nx,ny = x + dx, y + dy
        thing = (
            0 < x + 2 * dx < width-1 and
            0 < y + 2 * dy < height-1 and
            maze[nx, ny] == 0 and
            maze[x +2 * dx, y +2 * dy] == 0
        )
        if thing:
            maze[nx, ny] = 1
            maze [x + 2 * dx, y + 2 * dy] = 1
            c.append((x + 2 * dx, y + 2 * dy))
            break
    else:
        del c[ix]

for i in maze:
    print(''.join([(' ' if j == 1 else '#') for j in i]))

tk = Tk() 
c = Canvas(tk, width = width * cell_size, height = height * cell_size)
c.pack()
for i in xrange(width):
    for j in xrange(height):
        thing = maze[i,j]
        if thing == 0:
            color =  "pink"
        else:
            color = "white"
        c.create_rectangle(
            (i * cell_size, j * cell_size, i * cell_size + cell_size, j * cell_size + cell_size),
            fill = color 
        )

p = Player(maze, c)
p.id = c.create_rectangle(cell_size, cell_size, cell_size * 2, cell_size * 2, fill="red")

tk.bind('w', p.moveup)
tk.bind('s', p.movedown)
tk.bind('a', p.moveleft)
tk.bind('d', p.moveright)

tk.mainloop()

