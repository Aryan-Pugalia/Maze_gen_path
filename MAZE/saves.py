import json
import os
from setting import *

file_path = os.path.join(save_folder,f"saved_maze_{seed}.json")
def save_maze(grid, filename=file_path):
    maze_data = [[[tile.border for tile in row] for row in grid]]
    with open(filename, "w") as file:
        json.dump(maze_data, file)

def load_maze(grid, filename=file_path):
    try:
        with open(filename, "r") as file:
            maze_data = json.load(file)[0]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j].border = maze_data[i][j]
                grid[i][j].color = SELECT_COLOR
        return True
    except FileNotFoundError:
        return False