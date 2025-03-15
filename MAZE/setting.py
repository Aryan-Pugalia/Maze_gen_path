import pygame as py
import numpy as np
import os
py.init()
seed = 1
np.random.seed(seed)


# Dimensions
WIDTH = 600
HEIGHT = 600
ROW = 10
TILE_SIZE = HEIGHT/ROW
COL = int(WIDTH//TILE_SIZE)
#Colors
BLACK = 'black'
BASE_COLOR = (200,200,200) #grey
SELECT_COLOR = (250,250,250) #white
START = (250,150,0) #orange
END = (0,200,150) # greenish
TRACK = '#C371FF' #light purple
CHECK1 = '#BFEAA8'
CHECK2 = '#FFCF7D' #orangish
CLOCK = py.Clock()

#window

WINDOW = py.display.set_mode((WIDTH,HEIGHT))

SAVE = True
save_folder = 'Saves'

if not os.path.exists(save_folder):
    os.mkdir(save_folder)