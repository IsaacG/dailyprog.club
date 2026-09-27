"""Red Ridge Rendezvous

A workshop press feeds paper between two rubber rollers.
Roller A has `a` ridges around its circumference and roller B has `b`.
One ridge on each roller is painted red, and at the start the two red ridges are touching.

Once the press starts, each full turn of roller A turns roller B by exactly `a`/`b` of a turn.
The red ridges touch again only when roller B has completed a whole number of turns.
Return how many full turns of roller A must pass before the two red ridges touch for the first time since the start.

Constraints: `1 <= a <= 1,000,000,000` and `1 <= b <= 1,000,000,000`.
"""
import unittest
import math

def rollerMarks(a, b):
    """Return how many full turns of the first roller until both red ridges meet again."""
    return math.lcm(a, b) // a


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(rollerMarks(4, 6), 3)
        self.assertEqual(rollerMarks(6, 4), 2)
        self.assertEqual(rollerMarks(3, 9), 3)

if __name__ == "__main__":
    unittest.main()
