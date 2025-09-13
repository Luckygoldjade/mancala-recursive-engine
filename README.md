# Academic project completed in Fall 2022

## Project Title: Mancala Recursive Engine

A Python-based implementation of the classic two-player board game **Mancala**, designed as a text-based interface with recursive logic and private object-oriented state. The project focuses on implementing game mechanics such as sowing seeds, capturing, extra turns, and determining the winner using recursive logic and Python class design.

This project was completed as part of an academic course and demonstrates the use of recursion, private data members, and custom class design in Python.

---

## Key Features

- **Recursive turn logic:** Implements extra turn and capture rules using recursion.
- **Object-Oriented Programming:** Includes a `Mancala` class with private data members and helper methods.
- **Custom Player Class:** Players are created using a separate method and tracked throughout the game.
- **Board Management:** Pits and stores for both players are updated in real time using list-based storage.
- **Text Output:** All inputs and outputs are in simple text format—no GUI required.
- **Game State Tracking:** Supports checking for game end and determining the winner.
- **Error Handling:** Catches invalid moves and handles them gracefully.

---

## Tech Stack

- **Programming Language:** Python 3.x  
- **Dependencies:** None (standard library only)  
- **Project Type:** Terminal-based academic project with hardcoded test cases  
- **Optional:** Can be extended with unit tests using `pytest` (not required)

---

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Luckygoldjade/mancala-recursive-engine.git
   cd mancala-recursive-engine

2. **Run the Game**

    python Mancala.py


3. **Expected Output**
    The current setup runs a series of hardcoded play_game() calls and prints the game board and final winner. You can modify Mancala.py to test additional sequences.

---

## Screenshots

Below are screenshots from the terminal demo showing key parts of the game logic in action.

<p align="center"> <img src="docs/screenshots/demo_01.png" alt="Player 1 extra turn" width="700"/> </p> 
<p align="center"> <img src="docs/screenshots/demo_02.png" alt="Final board and winner" width="700"/> </p>
