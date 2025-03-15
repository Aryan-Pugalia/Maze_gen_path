import pygame as py
# import sys
import numpy as np
# import heapq
import json
from setting import *
from tile import Tile
py.init()

def create_grid():
    grid = [[Tile(i, j) for j in range(COL)] for i in range(ROW)]
    for i in range(ROW):
        for j in range(COL):
            grid[i][j].border_cells = {d: grid[i + dx][j + dy] if 0 <= i + dx < ROW and 0 <= j + dy < COL else None
                                       for d, (dx, dy) in {'u': (-1, 0), 'd': (1, 0), 'l': (0, -1), 'r': (0, 1)}.items()}
    return grid

def draw_board(grid):
    for i in range(ROW):
        for j in range(COL):
            grid[i][j].draw_border()
    py.display.update()

def remove_nb(next,current:Tile):
    mapping = ['u','d','l','r']
    index= list(current.border_cells.values()).index(next)
    current.border_cells[mapping[index]] = None

def remove_border(Next:Tile,Current:Tile):
    for d, r in [('u', 'd'), ('d', 'u'), ('l', 'r'), ('r', 'l')]:
        if Current.border_cells[d] == Next:
            Current.border[d], Next.border[r] = False, False

def create_maze(grid):
    
    draw_board(grid=grid)
    stack = []
    visited = set()
    Current:Tile= grid[0][0]
    stack.append(Current)
    visited.add(Current)
    while len(stack) != 0:
        Current.color = SELECT_COLOR
        if len(Current.ret_nb()) == 0:
            stack.pop()
            if len(stack) ==0:
                break
            Current = stack[-1]
            continue
        Next = Current.ret_nb()[-1]
        
        if Next in visited:
            remove_nb(Next,Current)
            continue
        visited.add(Next)
        stack.append(Next)
        
        remove_border(Next,Current)
        Next.color = SELECT_COLOR
        Current = Next
        CLOCK.tick(60)
        draw_board(grid)
