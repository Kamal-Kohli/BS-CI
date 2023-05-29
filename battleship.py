from random import randint
import time

"""
Legend:
1. "+" = Water or empty space.
2. "s" = Ship positions, part of the ship.
3. "o" = Water that was shot with bullets, a miss it hit no ship.
4. "x" = Ship sunk!

Battleship:
A. grid = 10x10
B. Player will have 50 bullets to take down ships.
C. 5 ships of variable length randomly placed.
D. Every hit and misses shot will be show up in the grid.
E. If all ships are unearthed before using up all bullets, You Win else, You Lose.
F. You can choose a row and column such as A:3, B:5 to indicate where to shoot.
"""

# Global constants
# Global variable for grid
GRID = [[]]
#Global variable of number of ships to place
NUM_SHIPS = 5
#Global variable for bullets left
BULLETS_LEFT = 50
#Global variable for game over
GAME_OVER = False
#Global varibale for ships sunk
NUM_OF_SHIPS_SUNK = 0
#Gloabal varibale for ship positions
SHIP_POSITIONS = [[]]

#Constants and globals
OCEAN = "."
FIRE = "X"
HIT = "*"
GRID_SIZE = 10
SHIPS = [5, 4, 3, 3, 2]

#globals
orientation = -1 # Stores the hit ship orientation. Determined on second hit
total_hits = [] # Stores the ship number every time AI hits a ship while ship is afloat
miss = 1 # Stores whether last AI shot was a miss

# Player variables
player_alive = 17 # -1 every time a ship is hit
player_radar = []
player_board = []

# CPU variables
cpu_alive = 17
cpu_radar = []
cpu_board = []
ship_position = [] 
ship_length = [] 

