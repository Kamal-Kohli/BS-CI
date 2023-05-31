# BS-CI
This is a simple implementation of the classic Battleship game in Python. The game is played on the command line interface and allows two players to take turns guessing the locations of each other's ships.

## USER EXPERIENCE - UX
+ [Rules](#rules "Rules")
+ [Rules](#rules "Rules")
+ [Wireframes](#wireframes "Wireframes")
+ [Features](#features "Features")
+ [Technologies used](#technologies-used "Technologies used")
+ [Editor](#editor "Editor")
+ [Unfixed bugs](#unfixed-bugs "Unfixed bugs")
+ [Testing](#testing "Testing")
+ [Deployment](#deployment "Deployment")
+ [Credits](#credits "Credits")

## Instructions
- Clone the repository or click on [Heroku](https://battleship-game-ci.herokuapp.com/) deplyed link.
- Clone the repository users run the following command `python3 run.py` in terminal or simply choose "Run code" by right click in Gitpod/CodeAnywhere users.
- The game will display two game boards, one for player and cpu. The boards are marked with coordinates and initially show only the player's own ships.
- The game will prompt you to enter the size of the game board (number of rows and columns). You can choose any positive integers, but keep in mind that larger game boards may take longer to play.
- The game will take turns between you and the computer. On your turn, you will be prompted to enter a target coordinate to attack. The computer will also display its attacks and the result of each attack.
- The game will continue until one player sinks all of the opponent's ships.
- Enjoy the game and have fun!

## Rules
1. Game has a 10x10 grid where they can place their ships.
2. Each player has a set of 5 ships that occupy multiple adjacent cells on the game board. Specifies the lengths of the ships. By default, it is set to [5, 4, 3, 3, 2]. You can modify this list to create ships of different lengths.
3. Players take turns guessing the coordinates of the opponent's ships by entering row and column numbers and alphabets e.g. A1, B1 etc.
4. The game indicates whether a ship was hit or missed.
5. If a ship is hit in all its cells, it is considered sunk.
6. The game ends when all the ships of one player are sunk.

## Design
Interface of BattleShip Game
![Game-Interface](/assets/images/game-interface.png)

## Customization
If you wish to customize the game, you can modify the following parameters in the `run.py` file:
- GRID_SIZE: Specifies the size of the game board. By default, it is set to 10x10.
- NUM_SHIPS: Specifies the number of ships each player has. By default, it is set to 5.
- SHIP: Specifies the lengths of the ships. By default, it is set to [5, 4, 3, 3, 2]. You can modify this list to create ships of different lengths.

## Code Structure
### - Constants and globals for the battle ship game:
![variables](/assets/images/Variables.png)

### - Gird and place ship to grid board with the variations of ships lengths:
![Grid & Ships](/assets/images/Place-ships.png)
![Grid & Ships](/assets/images/Add-ship-grid.png)

### - Ship HIT & Sunk!
![Hit and sunk](/assets/images/hit&sunk.png)

### - Start and Play game code
![Start](/assets/images/play.png)
![Play](/assets/images/game.png)

## Unfix bugs
I try to fix it my pep8 test, but still unfix bugs existing. In future I will try to fix them all. I asked support to slack but still it's not resolved. 
![pep8](/assets/images/pep8-test.png)



