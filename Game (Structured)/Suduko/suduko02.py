import random

class SudokuGenerator:
    def __init__(self, N=9, K=20):
        self.N = N  # Size of the grid (N x N)
        self.K = K  # Number of cells to remove (difficulty)
        self.grid = [[0 for _ in range(N)] for _ in range(N)]

    def fill_grid(self):
        self.fill_diagonal()
        self.fill_remaining(0, 3)

    def fill_diagonal(self):
        for i in range(0, self.N, 3):
            self.fill_box(i, i)

    def fill_box(self, row, col):
        nums = list(range(1, self.N + 1))
        random.shuffle(nums)
        for i in range(3):
            for j in range(3):
                self.grid[row + i][col + j] = nums.pop()

    def is_safe(self, row, col, num):
        return (
            self.not_in_row(row, num) and
            self.not_in_col(col, num) and
            self.not_in_box(row - row % 3, col - col % 3, num)
        )

    def not_in_row(self, row, num):
        return num not in self.grid[row]

    def not_in_col(self, col, num):
        return all(self.grid[row][col] != num for row in range(self.N))

    def not_in_box(self, box_start_row, box_start_col, num):
        return all(
            self.grid[row][col] != num
            for row in range(box_start_row, box_start_row + 3)
            for col in range(box_start_col, box_start_col + 3)
        )

    def fill_remaining(self, i, j):
        if i == self.N - 1 and j == self.N:
            return True
        if j == self.N:
            i += 1
            j = 0
        if i < 3:
            if j < 3:
                j = 3
        elif i < self.N - 3:
            if j == int(i / 3) * 3:
                j += 3
        else:
            if j == self.N - 3:
                i += 1
                j = 0
                if i == self.N:
                    return True

        for num in range(1, self.N + 1):
            if self.is_safe(i, j, num):
                self.grid[i][j] = num
                if self.fill_remaining(i, j + 1):
                    return True
                self.grid[i][j] = 0
        return False

    def remove_cells(self):
        count = self.K
        while count:
            row = random.randint(0, self.N - 1)
            col = random.randint(0, self.N - 1)
            if self.grid[row][col] != 0:
                self.grid[row][col] = 0
                count -= 1

    def generate_sudoku(self):
        self.fill_grid()
        self.remove_cells()
        return self.grid


def print_sudoku(grid):
    print("\n+-------+-------+-------+")
    for i, row in enumerate(grid):
        print("| " + " | ".join(
            " ".join(str(num) if num != 0 else "." for num in row[j:j + 3])
            for j in range(0, len(row), 3)
        ) + " |")
        if (i + 1) % 3 == 0:
            print("+-------+-------+-------+")


if __name__ == "__main__":
    sudoku = SudokuGenerator(N=9, K=30)
    puzzle = sudoku.generate_sudoku()
    print_sudoku(puzzle)
