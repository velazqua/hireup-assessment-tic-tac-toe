# Tic-Tac-Toe 

Welcome to the Tic-Tac-Toe console assessment! This task asks you to build a playable 3x3 Tic-Tac-Toe game for two players, with optional single-player mode against a simple AI.

---

##  Objective
Create a console Tic-Tac-Toe game where two players (X and O) take turns placing markers on a 3x3 board until one wins or the board is full.

---

## Learning Goals
- Manipulate lists (2D or flat list) to represent game state  
- Implement game rules and win/draw detection  
- Handle user input and validate moves  
- Structure code with functions for clarity and reusability  
- (Optional) Implement simple AI (random moves or basic blocking)

---

## Requirements (Detailed)

Your program must:

1. **Display a 3x3 board**. You may show cell numbers for empty cells to guide input, e.g. 1–9.  
2. **Allow players to select moves**, specifying a cell number (1–9) or row/column. Reject invalid or occupied moves with a helpful message and re-prompt.  
3. **Alternate turns** between Player X and Player O.  
4. **After each move**, display the updated board.  
5. **Detect win conditions** (three in a row horizontally, vertically, or diagonally) and announce the winner.  
6. **Detect a draw** (board full with no winner) and announce it.  
7. **Provide a way to restart** or exit after a game ends.  
8. **(Optional bonuses)**:
   - Single-player mode vs an AI (random or basic strategy).  
   - Keep a score tally across multiple games.  
   - Input via coordinates (row, col) as alternative to 1–9.  
   - Nice ASCII board formatting.


---

## Running the Program

1. Save your file as:
```
tictactoe.py
```
2. Run in terminal:
```bash
python tictactoe.py
```
or
```bash
python3 tictactoe.py
```

---

## Example Session

```
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

Player X, enter move (1-9): 5
...
Player O wins!
Play again? (yes/no): no
Goodbye!
```

---

## Bonus Ideas
- Implement a basic AI using random moves or a blocking strategy.  
- Track wins/losses/ties across a session.  
- Add a simple minimax implementation for an unbeatable AI (advanced).  
- Allow saving/loading match history.

---

## Submission

When finished:
```bash
git add tictactoe.py
git commit -m "Complete Tic-Tac-Toe assessment"
git push origin main
```

---

## Resources
- Python fundamentals: https://docs.python.org/3/tutorial/  
- Minimax algorithm (optional): many online tutorials and references

>  *Tip:* Start with two-player mode first; add AI only after core gameplay works.
