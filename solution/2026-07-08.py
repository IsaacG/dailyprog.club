"""Marbles in the Terrain

A marble rolls on an n×n terrain where each cell has a height given in heights (row-major order).
The marble starts at (startRow, startCol) facing startDir.
At each step, it looks at its four orthogonal neighbors (up, down, left, right).
It moves to the neighbor with the smallest height that is strictly lower than its current height.
If there is a tie, it chooses the first direction in the order: up, down, left, right.
After moving, it faces the direction of the move.
The marble stops when no neighbor has a lower height.
Record the complete trajectory, including the initial position: for each step, the row, column, and direction the marble is facing.
"""
DIRECTIONS = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}

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

assert marblePath(1, 0, 0, "down", [5]) == {"rows": [0], "cols": [0], "dirs": ["down"]}
assert marblePath(2, 0, 0, "right", [3, 2, 4, 1]) == {"rows": [0, 0, 1], "cols": [0, 1, 1], "dirs": ["right", "right", "down"]}
assert marblePath(2, 0, 0, "down", [2, 1, 1, 3]) == {"rows": [0, 1], "cols": [0, 0], "dirs": ["down", "down"]}
assert marblePath(2, 0, 0, "up", [0, 5, 5, 5]) == {"rows": [0], "cols": [0], "dirs": ["up"]}
assert marblePath(3, 0, 0, "right", [5, 4, 6, 3, 2, 8, 9, 1, 0]) == {"rows": [0, 1, 1, 2, 2], "cols": [0, 0, 1, 1, 2], "dirs": ["right", "down", "right", "down", "right"]}
