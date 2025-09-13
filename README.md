# Academic project completed in Fall 2022

Text-based Mancala engine in Python — demonstrates recursion by sowing one seed at a time with clean OOP game logic.

---

## Project Title: Mancala Recursive Engine

A Python-based implementation of the classic two-player board game Mancala, designed as a text-based interface with recursive logic and private object-oriented state.

I consciously chose recursion as the core technique to model seed-sowing. Each move in Mancala is like a courier dropping seeds one by one around a circular board. Recursion mirrors this process: drop one seed, move forward, and recurse until no seeds remain. This “count down one seed at a time” mental model made the logic intuitive, while also giving me practice with recursive function design — a skill often emphasized in software interviews.

This project was completed as part of an academic course and demonstrates the use of recursion, private data members, and custom class design in Python.

---

## Key Features

- **Recursive sowing logic:** Implements the game’s core mechanic by dropping one seed at a time via recursion, until the move is complete.
- **Recursive turn resolution:** Handles special cases (extra turns and captures) through recursive calls that continue or hand off play as rules dictate.
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
    ```bash
    python Mancala.py


3. **Expected Output**
    The current setup runs a series of hardcoded play_game() calls and prints the game board and final winner. You can modify Mancala.py to test additional sequences.

---

## Screenshots

Below are screenshots from the terminal demo showing key parts of the game logic in action.

<p align="center"> <img src="docs/screenshots/demo_01.png" alt="Player 1 extra turn" width="700"/> </p> 
<p align="center"> <img src="docs/screenshots/demo_02.png" alt="Final board and winner" width="700"/> </p>
