"""The Greenhouse Signal

A greenhouse is laid out as a grid of beds, stored in one flat array `beds`, with `width` beds per row, so `beds[row * width + column]` is `1` for a healthy bed and `0` for a bed that has pests.

At night, every bed that has pests at the start releases a pheromone straight along its whole row and straight along its whole column.
A healthy bed that shares a row or column with any such bed is flagged for treatment, and the record for the next morning marks it `0`.
Flagging is simultaneous: a bed flagged during the night does not release pheromones until a later night.

Return the flat array for the next morning: `0` where the bed shares its row or column with a bed that had pests at the start of the night, `1` otherwise.

Constraints: `1 <= n <= 4950`, where `n` is the number of beds in `beds`; `width` is an integer from `1` to `100` and divides `n`; every entry of `beds` is `0` or `1`.
"""
import unittest

def flagInfested(beds, width):
    """Return the flat grid for the next morning."""
    badRow = set()
    badCol = set()
    for row in range(len(beds) // width):
        for col in range(width):
            if beds[row * width + col] == 0:
                badRow.add(row)
                badCol.add(col)
    return [
        0 if row in badRow or col in badCol else 1
        for row in range(len(beds) // width)
        for col in range(width)
    ]


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(flagInfested([1, 1, 1, 1, 1, 1, 1, 1, 0], 3), [1, 1, 0, 1, 1, 0, 0, 0, 0])
        self.assertEqual(flagInfested([1, 1, 1, 1], 2), [1, 1, 1, 1])

if __name__ == "__main__":
    unittest.main()
