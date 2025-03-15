import pygame as py
import numpy as np
from setting import *

class Tile:
    def __init__(self,row,col):
        self.row = row
        self.col = col
        self.cord_y = row * TILE_SIZE
        self.cord_x = col * TILE_SIZE
        self.border = {'u':True,'d':True,'l':True,'r':True}
        self.color = BASE_COLOR
        self.border_cells= {}
        
        self.h = 0
        self.g = float('inf')
        self.f = self.g + self.h
        
        self.previous = None
        
    def __lt__(self,other):
        return self.f < other.f 
    
    def ret_nb(self): #return neighbor for generator
        nb = [i for i in self.border_cells.values() if i != None]
        return np.random.permutation(nb).tolist()
        
    
    def ret_nb_solver(self,grid):#return neighbor based on border for solver
        nb = []
        for direction, (dx, dy) in {'u': (-1, 0), 'd': (1, 0), 'l': (0, -1), 'r': (0, 1)}.items():
            if not self.border[direction]:
                nb.append(grid[self.row + dx][self.col + dy])
        return nb
    
    def draw_border(self):
        width = int(TILE_SIZE/20)
        self.draw_color()
        if self.border['u']:
            py.draw.line(WINDOW,BLACK,(self.cord_x,self.cord_y),(self.cord_x+TILE_SIZE,self.cord_y),width=width)
            
        if self.border['l']:
            py.draw.line(WINDOW,BLACK,(self.cord_x,self.cord_y),(self.cord_x,self.cord_y+TILE_SIZE),width=width)
            
        if self.border['r']:
            py.draw.line(WINDOW,BLACK,(self.cord_x+TILE_SIZE,self.cord_y),(self.cord_x+TILE_SIZE,self.cord_y+TILE_SIZE),width=width)
            
        if self.border['d']:
            py.draw.line(WINDOW,BLACK,(self.cord_x,self.cord_y+TILE_SIZE),(self.cord_x+TILE_SIZE,self.cord_y+TILE_SIZE),width=width)
            
    def draw_color(self):
        py.draw.rect(WINDOW,self.color, py.Rect(self.cord_x,self.cord_y,TILE_SIZE,TILE_SIZE))
      
