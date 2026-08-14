# Tic-Tac-Toe

A simple command-line Tic-Tac-Toe game built with Python. The player plays against the computer, which selects its moves randomly.

## Project Overview

This project was created to practice Python fundamentals by building a small interactive game.

The game uses a 3x3 board where:

- The computer plays as `X`.
- The human player plays as `O`.
- The computer selects an available position randomly.
- The player enters a position from 1 to 9.
- The game checks for a winner after each move.
- The game ends when a player wins or all positions are occupied.

## Features

- 3x3 Tic-Tac-Toe board
- Human vs. computer gameplay
- Random computer moves
- Free-field detection
- Row, column, and diagonal win detection
- Tie detection
- Command-line input

## Python Concepts Practiced

- Lists and nested lists
- Functions
- `for` loops
- `while` loops
- Conditional statements
- User input
- Type conversion
- Tuples
- The `random` module
- List operations
- Function parameters
- Boolean values

## Project Structure

```text
tic-tac-tie/
│
├── main.py
└── README.md

How to Run

Make sure Python is installed on your computer.

Clone the repository:

git clone https://github.com/pamarthichetana/tic-tac-tie.git

Move into the project directory:

cd tic-tac-tie

Run the program:

python main.py

How to Play
The board contains positions from 1 to 9:
1 2 3
4 5 6
7 8 9

Enter the number corresponding to the position where you want to place your move.

The computer will automatically select one of the remaining positions.
The game continues until:

1. The computer wins.
2. The player wins.
3. All positions are occupied and the game ends in a tie.

## Future Improvements

- Add input validation for invalid entries.
- Prevent the program from crashing when non-numeric input is entered.
- Improve the board display.
- Add a smarter computer opponent.
- Add difficulty levels.
- Add the option to play multiple rounds.
- Keep track of wins, losses, and ties.

## Author

Chetana Pamarthi
