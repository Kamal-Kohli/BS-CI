from random import randint
import time

"""
Legend:
1. "." = Water or empty space.
2. "s" = Ship positions, part of the ship.
3. "o" = Water that was shot with bullets, a miss it hit no ship.
4. "x" = Ship Hit!

Battleship:
A. grid = 10x10
B. Player will have 50 bullets to take down ships.
C. 5 ships of variable length randomly placed.
D. Every hit and misses shot will be show up in the grid.
E. If all ships are unearthed before using up all bullets, You Win else, You Lose.
F. You can choose a row and column such as A:3, B:5 to indicate where to shoot.
"""

#Constants and globals
EMPTY = '.'
SHIP = 'S'
HIT = 'X'
MISS = 'O'
GRID_SIZE = 10 # Numbr of ships each grid
SHIPS = [5, 4, 3, 3, 2] # Variation sizes of ships

# Player variables
player_alive = 17 
player_radar = []
player_board = []

# CPU variables
cpu_alive = 17
cpu_radar = []
cpu_board = []
ship_position = [] 
ship_length = [] 

# Function to create an empty grid
class Grid:
    def __init__(self):
        self.grid = [[EMPTY] * GRID_SIZE for _ in range(GRID_SIZE)]
        self.ships = []
    