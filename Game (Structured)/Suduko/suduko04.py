import curses
import os


class SudokuGame:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.solution = [row[:] for row in puzzle]  # Copy for validation
        self.cursor = [0, 0]  # Starting position of the cursor (row, col)

    def is_safe(self, row, col, num):
        """Check if it's safe to place the number in the cell."""
        return (
            all(self.puzzle[row][j] != num for j in range(9)) and
            all(self.puzzle[i][col] != num for i in range(9)) and
            all(
                self.puzzle[i][j] != num
                for i in range(row - row % 3, row - row % 3 + 3)
                for j in range(col - col % 3, col - col % 3 + 3)
            )
        )

    def draw_grid(self, stdscr):
        """Draw the Sudoku grid with the current state."""
        stdscr.clear()
        stdscr.addstr("\n  Arrow Keys: Move | Numbers: Fill Cell | Backspace: Clear | Q: Quit\n")
        stdscr.addstr("  +-------+-------+-------+\n")

        for i, row in enumerate(self.puzzle):
            row_str = " | ".join(
                " ".join(str(num) if num != 0 else "." for num in row[j:j + 3])
                for j in range(0, len(row), 3)
            )
            stdscr.addstr(f"  | {row_str} |\n")

            if (i + 1) % 3 == 0:
                stdscr.addstr("  +-------+-------+-------+\n")

        # Highlight the cursor
        stdscr.addstr(2 + self.cursor[0] * 2, 3 + self.cursor[1] * 2, " ", curses.A_REVERSE)

    def play(self, stdscr):
        """Main interactive loop."""
        curses.curs_set(0)  # Hide the terminal cursor

        while True:
            self.draw_grid(stdscr)
            key = stdscr.getch()

            if key == curses.KEY_UP and self.cursor[0] > 0:
                self.cursor[0] -= 1
            elif key == curses.KEY_DOWN and self.cursor[0] < 8:
                self.cursor[0] += 1
            elif key == curses.KEY_LEFT and self.cursor[1] > 0:
                self.cursor[1] -= 1
            elif key == curses.KEY_RIGHT and self.cursor[1] < 8:
                self.cursor[1] += 1
            elif ord('1') <= key <= ord('9'):
                num = int(chr(key))
                row, col = self.cursor
                if self.puzzle[row][col] == 0 and self.is_safe(row, col, num):
                    self.puzzle[row][col] = num
            elif key == curses.KEY_BACKSPACE:
                row, col = self.cursor
                if self.puzzle[row][col] != 0:
                    self.puzzle[row][col] = 0
            elif chr(key).lower() == 'q':
                break


if __name__ == "__main__":
    # Predefined Sudoku puzzle (0s represent empty cells)
    sudoku_puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    curses.wrapper(SudokuGame(sudoku_puzzle).play)
