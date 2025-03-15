import heapq
from tile import Tile
from setting import *
from maze_gen import draw_board
py.init()



def distance(i,j,x,y):
    return (abs(x-i)**2 + abs(y-j))

def maze_solver_A(start_pos: tuple[int], end_pos: tuple[int], grid: list[list[Tile]]) -> None:
    open_list = []
    close_list = []
    start: Tile = grid[start_pos[0]][start_pos[1]]
    end: Tile = grid[end_pos[0]][end_pos[1]]
    start.g = 0
    start.h = distance(start_pos[0], start_pos[1], end_pos[0], end_pos[1])
    
    heapq.heappush(open_list, start)
    current = None
    while len(open_list) != 0 or current == end:
        current: Tile = heapq.heappop(open_list)
        if current == end:
            print("Found")
            break
        else:
            if current != start:
                current.color = CHECK2
            close_list.append(current)
            
            for nb in current.ret_nb_solver(grid):
                g = current.g + 1
                h = distance(nb.row, nb.col, end.row, end.col)
                if nb in open_list or nb in close_list:
                    if g < nb.g:
                        nb.g = g
                        nb.previous = current
                else:
                    nb.g = g
                    nb.h = h
                    nb.previous = current
                    if nb != start:
                        if nb != end:
                            nb.color = CHECK1
                    CLOCK.tick(100)
                    draw_board(grid)
                    heapq.heappush(open_list, nb)
    # Backtrack
    
    while current != start:
        CLOCK.tick(100)
        if current != end:
            current.color = TRACK
        current = current.previous
        
        draw_board(grid)
