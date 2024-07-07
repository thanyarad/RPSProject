# Rock, Paper, Scissors Game (V sem Python Mini Project)

## Overview

This is a simple Rock, Paper, Scissors game implemented in Python using the Tkinter library for the graphical user interface. The game allows a player to compete against the computer, keeping track of scores and updating the display accordingly.

## Features

- Graphical user interface built with Tkinter.
- Interactive gameplay where the player can select rock, paper, or scissors.
- Randomized computer choices.
- Score tracking for both player and computer.
- Visual feedback with images representing rock, paper, and scissors.

## Prerequisites

- Python 3.x
- Tkinter library
- PIL (Pillow) library for image handling

## Installation

1. **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install the required libraries:**

    ```bash
    pip install tkinter pillow
    ```

3. **Ensure the following directory structure for images:**

    ```
    images/
    ├── paper_computer.png
    ├── paper_player.png
    ├── rock_computer.png
    ├── rock_player.png
    ├── scissor_computer.png
    ├── scissor_player.png
    ```

## Usage

1. **Navigate to the project directory:**

    ```bash
    cd <repository-directory>
    ```

2. **Run the game:**

    ```bash
    python Source.py
    ```

3. **Gameplay Instructions:**
    - Click on the buttons to select your move: Rock, Paper, or Scissors.
    - The computer will randomly select a move.
    - The scores will be updated based on the outcome of each round.
    - The first to reach 5 points wins the game.

## Code Explanation

- **Import Statements:**
  - `tkinter` is used for creating the GUI.
  - `PIL (Pillow)` is used for image handling.
  - `randint` from `random` is used for the computer's random choice.

- **GUI Setup:**
  - The main window is created and configured with a title and background color.
  - Images are loaded and displayed for both player and computer choices.
  - Labels are used to display the score and player/computer indicators.

- **Functions:**
  - `updatemsg(message)`: Updates the final message label with the given message.
  - `player_update()`: Increments the player's score.
  - `computer_update()`: Increments the computer's score.
  - `win_check(player_choice, computer_choice)`: Checks the outcome of the game and updates scores and messages accordingly.
  - `choice_update(player_choice)`: Updates the displayed choices and checks the game outcome.

- **Buttons:**
  - Buttons are created for each move (Rock, Paper, Scissors) with corresponding images and commands to handle player input.

## Screenshots

![Game Interface](D:\Pictures\Screenshots\Screenshot (119).png)  *(Replace with actual screenshot path)*

## Contributing

Feel free to fork the repository and submit pull requests. Contributions are welcome!
