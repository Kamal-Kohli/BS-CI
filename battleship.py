import random
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
#Global variable for grd size
GRID_SIZE = 10
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


# Create the game board
myBoard = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Create the ships
ships = []
for _ in range(NUM_SHIPS):
    ship_row = random.randint(0, GRID_SIZE - 1)
    ship_col = random.randint(0, GRID_SIZE - 1)
    ships.append([ship_row, ship_col])

# Function to print the game board
def print_board():
    print("   " + " ".join(str(i) for i in range(GRID_SIZE)))
    print("   " + "---" * GRID_SIZE)
    for row in range(GRID_SIZE):
        print(f"{row} | {' | '.join(grid[row])} |")
        print("   " + "---" * GRID_SIZE)