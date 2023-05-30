import random

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
E. If all ships are unearthed before using up all bullets, 
    You Win else, You lose.
F. You can choose a row and column such as A1, B1 to indicate where to shoot.
"""

# Constants and globals
EMPTY = '.'
SHIP = 'S'
HIT = 'X'
MISS = 'O'
GRID_SIZE = 10  # Numbr of ships each grid
SHIPS = [5, 4, 3, 3, 2]  # Variation sizes of ships
NUM_SHIPS = len(SHIPS)


class Grid:  # Function to create an empty grid
    def __init__(self):
        self.grid = [[EMPTY] * GRID_SIZE for _ in range(GRID_SIZE)]
        self.ships = []
        
    # Function to randomly place ships on the grid

    def place_ships(self):
        for size in SHIPS:
            ship_placed = False
            while not ship_placed:
                row = random.randint(0, GRID_SIZE - 1)
                col = random.randint(0, GRID_SIZE - 1)
                direction = random.choice(['horizontal', 'vertical'])

                if self.can_place_ship(row, col, size, direction):
                    self.add_ship(row, col, size, direction)
                    ship_placed = True
    # Function to place ship to grid

    def can_place_ship(self, row, col, size, direction):
        if direction == 'horizontal':
            if col + size > GRID_SIZE:
                return False

            for c in range(col, col + size):
                if self.grid[row][c] == SHIP:
                    return False
        else:
            if row + size > GRID_SIZE:
                return False

            for r in range(row, row + size):
                if self.grid[r][col] == SHIP:
                    return False

        return True
    # Function to add ships on the grid

    def add_ship(self, row, col, size, direction):
        if direction == 'horizontal':
            for c in range(col, col + size):
                self.grid[row][c] = SHIP
        else:
            for r in range(row, row + size):
                self.grid[r][col] = SHIP

        self.ships.append((row, col, size, direction))
    # Function to Print/Dispaly the grid to Board

    def print_grid(self, hide_ships=True):
        print('   ', end='')
        for i in range(GRID_SIZE):
            print(chr(i + ord('A')), end=' ')
        print()

        for i, row in enumerate(self.grid):
            print(f'{i + 1:2}', end=' ')
            for cell in row:
                if hide_ships and cell == SHIP:
                    print(EMPTY, end=' ')
                else:
                    print(cell, end=' ')
            print()
    # Function to validate move

    def is_valid_move(self, row, col):
        if row < 0 or row >= GRID_SIZE or col < 0 or col >= GRID_SIZE:
            return False

        cell = self.grid[row][col]
        return cell != HIT and cell != MISS

    def make_move(self, row, col):
        if not self.is_valid_move(row, col):
            return False

        if self.grid[row][col] == SHIP:
            self.grid[row][col] = HIT
            self.check_ship_sunk(row, col)
            return True
        else:
            self.grid[row][col] = MISS
            return False
    
    def check_ship_sunk(self, row, col):  # Function to hit ship display sunk 
        for ship in self.ships:
            r, c, size, direction = ship

            if direction == 'horizontal':
                if row == r and col >= c and col < c + size:
                    for i in range(c, c + size):
                        if self.grid[row][i] != HIT:
                            return
                else:
                    continue
            else:
                if col == c and row >= r and row < r + size:
                    for i in range(r, r + size):
                        if self.grid[i][col] != HIT:
                            return
                else:
                    continue

            # All cells of the ship have been hit, mark it as sunk
            for i in range(size):
                if direction == 'horizontal':
                    self.grid[row][c + i] = HIT
                else:
                    self.grid[r + i][col] = HIT
            print('Ship Sunk!')
# Function to example to how to choose row & col, indicate shoot area


def get_move_from_input():  
    move = input('Enter your move (e.g., A5): ')
    col = ord(move[0].upper()) - ord('A')
    row = int(move[1:]) - 1
    return row, col


def play_game():  # Function to start game

    player_grid = Grid()
    cpu_grid = Grid()

    player_grid.place_ships()
    cpu_grid.place_ships()

    player_turn = True
    # Function to play turn to Player and Cpu
    while True:
        if player_turn:
            print('Player Grid:')
            player_grid.print_grid(hide_ships=False)
            print('Cpu Grid:')
            cpu_grid.print_grid()

            print('Player\'s Turn')
            row, col = get_move_from_input()
            if cpu_grid.make_move(row, col):
                print('Hit!')
            else:
                print('Miss!')

            if all(cell == HIT for row in cpu_grid.grid for cell in row):
                print('Congratulations! You won!')
                break
        else:
            print('Player Grid:')
            player_grid.print_grid(hide_ships=False)
            print('Cpu Grid:')
            cpu_grid.print_grid(hide_ships=True)

            print('CPU\'s Turn')
            row = random.randint(0, GRID_SIZE - 1)
            col = random.randint(0, GRID_SIZE - 1)
            if player_grid.make_move(row, col):
                print('Hit!')
            else:
                print('Miss!')

            if all(cell == HIT for row in player_grid.grid for cell in row):
                print('Sorry, you lost!')
                break

        player_turn = not player_turn


play_game()
