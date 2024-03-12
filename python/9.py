import tkinter as tk
import random

def generate_sudoku():
    base = 3
    side = base * base

    # Pattern for a baseline valid solution
    def pattern(r, c): return (base * (r % base) + r // base + c) % side

    # Randomly permuting rows, columns and numbers (of valid base pattern)
    def shuffle(s): return random.sample(s, len(s))

    rBase = range(base)
    rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, base * base + 1))

    # Produce board using randomized baseline pattern
    board = [[nums[pattern(r, c)] for c in cols] for r in rows]

    return board

class SudokuApp:
    def __init__(self, master):
        self.master = master
        master.title("Sudoku")

        self.board = generate_sudoku()

        for i in range(9):
            for j in range(9):
                entry = tk.Entry(master, width=2, font=('Arial', 16), justify="center", bd=5)
                entry.grid(row=i, column=j)
                entry.insert(0, str(self.board[i][j]))
                entry.config(state='disabled' if random.random() < 0.5 else 'normal')

# Create the main Tkinter window
root = tk.Tk()
app = SudokuApp(root)

# Run the Tkinter event loop
root.mainloop()
