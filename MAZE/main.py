import pygame as py
from tile import Tile
from maze_gen import create_grid,create_maze,draw_board
from saves import load_maze,save_maze
from maze_solver import maze_solver_A
from setting import *
import sys
py.init()



py.display.set_caption("Maze Generation")

def main():
    GRID : list[list[Tile]] = create_grid() 
    maze_done = False
    start_pos_given = False
    end_pos_given = False
    
    while True:
        
        for event in py.event.get():
            if event.type == py.QUIT:
                sys.exit()
            if event.type == py.KEYDOWN and not maze_done:
                if event.key == py.K_SPACE:
                    if not load_maze(GRID):
                        create_maze(GRID)
                        save_maze(GRID)
                    maze_done = True
            if maze_done:
                if event.type == py.MOUSEBUTTONUP:
                    
                    if not start_pos_given:
                        start_pos = py.mouse.get_pos()
                        start_pos = list([int(i//TILE_SIZE) for i in start_pos])[::-1]
                        start_pos_given = True
                        GRID[start_pos[0]][start_pos[1]].color = START  
                        
                    if start_pos_given and not end_pos_given:
                        end_pos = py.mouse.get_pos()
                        end_pos = list([int(i//TILE_SIZE) for i in end_pos])[::-1]
                        if end_pos == start_pos:
                            continue
                        else:
                            end_pos_given = True
                            GRID[end_pos[0]][end_pos[1]].color = END  
                            
                if start_pos_given and end_pos_given and event.type == py.KEYDOWN:
                    maze_solver_A(start_pos,end_pos,GRID)
        
        draw_board(GRID)

if __name__=='__main__':    
    main()
    py.quit()