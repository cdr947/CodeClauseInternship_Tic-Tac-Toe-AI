# CodeClauseInternship_Tic-Tac_Toe_AI

# Tic Tac Toe Game with AI

This is a Tic Tac Toe game implemented in Python using the `tkinter` library for the graphical user interface (GUI). The game features an AI opponent powered by the minimax algorithm.

## Features

- Player can choose to play as 'X' or 'O'.
- AI opponent using the minimax algorithm for optimal moves.
- Interactive GUI with a 3x3 grid for the game board.

## Requirements

- Python 3.x
- `tkinter` library (included with most Python installations)

## Installation

1. Clone the repository or download the source code files.

    ```sh
    git clone https://github.com/cdr947/CodeClauseInternship_Tic-Tac-Toe-AI.git
    cd CodeClauseInternship_Tic-Tac-Toe-AI
    ```

2. Ensure you have Python 3 installed. You can download it from [python.org](https://www.python.org/).

## Usage

1. Run the `index.py` script.

    ```sh
    python index.py
    ```

2. A window will appear. Choose your symbol ('X' or 'O') to start the game.

3. Play against the AI by clicking on the grid cells. The AI will make its move after you.

4. The game will display a message when there is a winner or if the game is a tie.

## Code Overview

### Minimax Algorithm

The AI opponent uses the minimax algorithm to evaluate the best possible move at each turn. This ensures that the AI plays optimally.

### Main Classes and Functions

- `TicTacToe`: The main class that initializes the game, handles player and AI moves, and manages the GUI.
- `create_initial_screen`: Displays the initial screen for symbol selection.
- `start_game`: Initializes the game board and starts the game.
- `create_buttons`: Creates the game buttons (grid cells).
- `button_click`: Handles player moves.
- `ai_move`: Calculates and makes the AI's move.
- `minimax`: The minimax algorithm implementation for the AI.
- `check_winner`: Checks if there is a winner.
- `game_over`: Displays the game over message and closes the window.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgements

- The `tkinter` library for providing the GUI components.
- Various online resources for tutorials on the minimax algorithm and `tkinter`.
