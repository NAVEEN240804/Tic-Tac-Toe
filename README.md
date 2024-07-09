# Tic-Tac-Toe with AI Opponent
This project implements a Tic-Tac-Toe game in Python where you can play against an AI opponent using the A* search algorithm with a heuristic evaluation function. The AI opponent tries to make optimal moves based on the current board state.

## Features
- **Player vs AI:** Play against a computer opponent that uses A* search and a heuristic evaluation to make moves.
- **Simple CLI Interface:** User-friendly command-line interface for playing the game.
- **Depth-Limited Search:** Control the depth of the AI's search to adjust difficulty.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/your-username/tic-tac-toe-ai.git
   cd tic-tac-toe-ai
   ```
2. Ensure you have Python 3 installed.
3. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```
   
## Usage
Run the game from the command line:
```
python tic_tac_toe.py
```
Follow the on-screen instructions to play against the AI. Enter row and column numbers (0-2) to make your move.
## Example
```
$ python tic_tac_toe.py

Welcome to Tic-Tac-Toe!
Choose your move by entering row and column numbers (0-2).
You are 'X', and the AI is 'O'.

   |   |  
---------
   |   |  
---------
   |   |  

YOUR MOVE:
Enter row (0-2): 1
Enter column (0-2): 1

   |   |  
---------
   | X |  
---------
   |   |  

AI is making a move...

   | O |  
---------
   | X |  
---------
   |   |  

...
AI WINS!
```
## Contributions
NAVEEN240804 is the only contributor on this project
