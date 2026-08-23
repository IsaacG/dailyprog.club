"""The Silver Ewer

On the third night of the waxing moon, Sister Lune hangs her glass dew bells among the moonflowers.
As the night deepens, dew beads inside every bell, and before dawn she gathers each gleaming mouthful into the silver ewer.
The Work forbids carrying water where it does not wish to go: she tips the whole ewer over a single bed, and the garden takes it from there.

The garden is a terraced plot of beds. `heights` lists each bed's terrace height, row by row: the plot is `width` beds across, and the bed in row r, column c stands at height `heights[r * width + c]`.
Sister Lune tips the ewer over the bed at row `startRow`, column `startCol`, and that bed is soaked at once.

Water seeps from a soaked bed into any bed directly beside it (up, down, left, or right) that stands no higher than the bed the water is leaving.
It runs down the terraces and across level ground, but it never climbs: once it has fallen, it cannot rise again, not even to a height it has already passed through.
Every bed the water can reach this way is soaked in turn.

Return the number of soaked beds, counting the bed where the ewer was tipped.

Constraints: `1 <= n <= 400`, where `n` is the number of beds in `heights`; `width` divides `n`, with `1 <= width <= n`; each height is an integer from `0` to `9`; `0 <= startRow < n / width` and `0 <= startCol < width`.
"""
import unittest
import collections

def soakedBeds(heights, width, startRow, startCol):
    """Count the beds soaked by the water tipped at startRow, startCol."""
    todo = collections.deque([(startCol, startRow)])
    seen = {(startCol, startRow)}
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    h = {
        (x, y): heights[x + y * width]
        for y in range(len(heights) // width)
        for x in range(width)
    }
    while todo:
        x, y = todo.popleft()
        cur_h = h[x, y]
        for dx, dy in directions:
            pos = x + dx, y + dy
            if pos not in seen and pos in h and h[pos] <= cur_h:
                seen.add(pos)
                todo.append(pos)
    return len(seen)


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(soakedBeds([3, 2, 2, 5, 4, 1, 2, 1, 1, 1, 4, 4], 4, 0, 0), 8)
        self.assertEqual(soakedBeds([2, 2, 3, 1, 0, 0], 3, 1, 1), 2)
        self.assertEqual(soakedBeds([7], 1, 0, 0), 1)

if __name__ == "__main__":
    unittest.main()
