"""Where the Rain Goes

After a storm, a raindrop lands on a rooftop divided into an n by n grid of cells.
Each cell has an elevation, and these elevations are given as a flat list `heights`, read row by row: `heights[r * n + c]` is the elevation of the cell at row r, column c.
The drop starts at the cell given by `startRow` and `startCol`, facing up, and it will roll downhill.

### How the Drop Moves

Directions use screen orientation: up decreases the row number by 1, right increases the column number by 1, down increases the row number by 1, left decreases the column number by 1.

At each step, the drop considers the four cells directly up, right, down, and left of its current cell that are still on the roof.
It moves to the neighbor with the lowest elevation, but only if that elevation is strictly lower than the elevation of its current cell.
If the lowest elevation is shared by two or more neighbors, it chooses the first one in this fixed order: up, right, down, left.
The drop then faces the direction it moved.
When no neighbor is strictly lower, the drop stops.

### What to Return

Return the drop's full path as a structure with three equal-length arrays.
Index 0 is the starting cell before any move, with direction `"up"`; every later index is one move. `rows[i]` and `cols[i]` are the row and column at step i, and `dirs[i]` is the direction the drop faces at step i: `"up"`, `"right"`, `"down"`, or `"left"`.

Constraints: 1 <= n <= 6. `startRow` and `startCol` are inside the roof. `heights` has n\*n entries, each an integer from 0 to 9.
"""
import unittest

def raindropPath(n, startRow, startCol, heights):
    return marblePath(n, startRow, startCol, "up", heights)

DIRECTIONS = {"up": (0, -1), "right": (1, 0), "down": (0, 1), "left": (-1, 0)}

# 2026-07-08
def marblePath(n, startRow, startCol, startDir, heights):
    rows, cols, dirs = [], [], []
    def record(row, col, facing):
        rows.append(row)
        cols.append(col)
        dirs.append(facing)
    # record(...) the start, then each move of the marble until it settles
    board = {
        (x, y): height
        for y in range(len(heights) // n)
        for x, height in enumerate(heights[n * y:n * (n + 1)])
    }
    row, col, facing = startRow, startCol, startDir
    next_facing = startDir
    next_pos = startCol, startRow
    while next_facing:
        facing = next_facing
        col, row = next_pos
        record(row, col, facing)

        next_facing = ""
        next_best = board[col, row]
        for name, (dx, dy) in DIRECTIONS.items():
            if (v := board.get((col + dx, row + dy))) is not None and v < next_best:
                next_best = v
                next_pos = col + dx, row + dy
                next_facing = name

    return {"rows": rows, "cols": cols, "dirs": dirs}


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(raindropPath(3, 0, 0, [8, 7, 6, 5, 4, 3, 2, 1, 0]), {"rows": [0, 1, 2, 2, 2], "cols": [0, 0, 0, 1, 2], "dirs": ["up", "down", "down", "right", "right"]})
        self.assertEqual(raindropPath(3, 1, 1, [6, 3, 2, 5, 5, 3, 4, 4, 4]), {"rows": [1, 0, 0], "cols": [1, 1, 2], "dirs": ["up", "up", "right"]})
        self.assertEqual(raindropPath(1, 0, 0, [4]), {"rows": [0], "cols": [0], "dirs": ["up"]})
        self.assertEqual(raindropPath(2, 0, 0, [2, 2, 3, 4]), {"rows": [0], "cols": [0], "dirs": ["up"]})
        self.assertEqual(raindropPath(2, 0, 0, [3, 2, 1, 0]), {"rows": [0, 1, 1], "cols": [0, 0, 1], "dirs": ["up", "down", "right"]})
        self.assertEqual(raindropPath(3, 1, 1, [6, 6, 4, 7, 5, 3, 8, 3, 1]), {"rows": [1, 1, 2], "cols": [1, 2, 2], "dirs": ["up", "right", "down"]})
        self.assertEqual(raindropPath(6, 1, 1, [9, 9, 9, 9, 9, 9, 9, 8, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 7, 6, 5, 4, 4, 4, 7, 6, 6, 3, 2, 2, 7, 6, 2, 2, 1, 0]), {"rows": [1, 1, 2, 3, 3, 4, 4, 5, 5], "cols": [1, 2, 2, 2, 3, 3, 4, 4, 5], "dirs": ["up", "right", "down", "down", "right", "down", "right", "down", "right"]})

if __name__ == "__main__":
    unittest.main()
