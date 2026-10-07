"""#102 · 5 solvers (80% on first try)
The Orchardist's Stakes
=======================

An orchardist plants saplings on a flat field and marks each one with a stake.
Every stake sits at a whole-number position `[x, y]` in metres, and no two stakes share the same spot.

A taut wire runs straight across the field and counts as one guide line when it passes through the tops of at least two stakes.
A guide line has no ends, so two wires are the same guide line exactly when they touch exactly the same stakes.

Given `points`, a list of stakes where `points[i]` is the pair `[x, y]` of metre positions of stake i, return how many different guide lines the stakes define.

### Constraints

* 1 to 25 stakes, so the number of stakes is between 1 and 25.
* Every coordinate is an integer from 0 to 1000 inclusive.
* No two stakes share both coordinates.
"""
import unittest

import fractions
import itertools

def line(a, b):
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    if dx == 0:
        return (a[0], None)
    m = fractions.Fraction(dy, dx)
    i = a[1] - m * a[0]
    return (i, m)

def countLines(points):
    """Return how many distinct straight lines pass through at least two of the points."""
    return len({line(a, b) for a, b in itertools.combinations(points, r=2)})


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(countLines([[2,6], [5,5], [8,4]]), 1)
        self.assertEqual(countLines([[0, 0], [1, 3], [2, 1]]), 3)
        self.assertEqual(countLines([[0, 0], [4, 0], [0, 4], [4, 4]]), 6)
        self.assertEqual(countLines([[0, 0], [2, 2], [5, 5]]), 1)
        self.assertEqual(countLines([[0, 0], [7, 3]]), 1)
        self.assertEqual(countLines([[3, 4]]), 0)
        self.assertEqual(countLines([[5, 7], [5, 0], [5, 3]]), 1)
        self.assertEqual(countLines([[0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1], [0, 2], [1, 2], [2, 2]]), 20)
        self.assertEqual(countLines([[0, 0], [1, 0], [1, 1], [0, 1]]), 6)
        self.assertEqual(countLines([[0, 0], [1, 2], [2, 4], [3, 6]]), 1)
        self.assertEqual(countLines([[0, 0], [1, 1], [0, 2], [1, 3]]), 6)
        self.assertEqual(countLines([[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81], [10, 100], [11, 121], [12, 144], [13, 169], [14, 196], [15, 225], [16, 256], [17, 289], [18, 324], [19, 361], [20, 400], [21, 441], [22, 484], [23, 529], [24, 576]]), 300)

if __name__ == "__main__":
    unittest.main()
