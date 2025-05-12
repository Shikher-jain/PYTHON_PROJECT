import tkinter as tk
from tkinter import messagebox

class SudokuSolver:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.root.geometry("400x500")
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.create_grid()
        self.create_buttons()

    def create_grid(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)
        
        for row in range(9):
            for col in range(9):
                entry = tk.Entry(frame, width=2, font=("Arial", 16), justify="center")
                entry.grid(row=row, column=col, padx=5, pady=5, ipadx=5, ipady=5)
                self.cells[row][col] = entry

    def create_buttons(self):
        solve_button = tk.Button(self.root, text="Solve", command=self.solve_puzzle, bg="lightgreen", font=("Arial", 14))
        solve_button.pack(pady=10)

        clear_button = tk.Button(self.root, text="Clear", command=self.clear_grid, bg="lightcoral", font=("Arial", 14))
        clear_button.pack(pady=10)

    def get_puzzle(self):
        puzzle = []
        for row in self.cells:
            current_row = []
            for cell in row:
                value = cell.get()
                if value.isdigit():
                    current_row.append(int(value))
                else:
                    current_row.append(0)
            puzzle.append(current_row)
        return puzzle

    def set_puzzle(self, puzzle):
        for row in range(9):
            for col in range(9):
                if puzzle[row][col] != 0:
                    self.cells[row][col].delete(0, tk.END)
                    self.cells[row][col].insert(0, str(puzzle[row][col]))
                else:
                    self.cells[row][col].delete(0, tk.END)

    def clear_grid(self):
        for row in range(9):
            for col in range(9):
                self.cells[row][col].delete(0, tk.END)

    def is_valid(self, puzzle, row, col, num):
        for i in range(9):
            if puzzle[row][i] == num or puzzle[i][col] == num:
                return False
        box_row, box_col = row // 3 * 3, col // 3 * 3
        for i in range(3):
            for j in range(3):
                if puzzle[box_row + i][box_col + j] == num:
                    return False
        return True

    def solve(self, puzzle):
        for row in range(9):
            for col in range(9):
                if puzzle[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(puzzle, row, col, num):
                            puzzle[row][col] = num
                            if self.solve(puzzle):
                                return True
                            puzzle[row][col] = 0
                    return False
        return True

    def solve_puzzle(self):
        puzzle = self.get_puzzle()
        if self.solve(puzzle):
            self.set_puzzle(puzzle)
            messagebox.showinfo("Sudoku Solver", "Solved Successfully!")
        else:
            messagebox.showerror("Sudoku Solver", "No solution exists.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolver(root)
    root.mainloop()
