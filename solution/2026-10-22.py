"""The Violin Maker's Bench

A violin maker lines up the offcuts left over from a day's carving on the bench, one behind another, and checks how badly the row lurches from piece to piece.
The lurch of a row is the largest absolute difference between any two pieces lying side by side; a row of one piece does not lurch at all.

Given `values`, the lengths of the offcuts in millimetres, return the smallest lurch any ordering of all of them can achieve.
Each offcut is placed exactly once.

### Constraints

* `values` holds between 1 and 13 lengths
* every length is an integer from 0 to 1000 inclusive
"""
import unittest

import itertools
def smallestLurch(values):
    # TODO: return the smallest possible largest neighbor difference
    return max((b - a for a, b in itertools.pairwise(sorted(values))), default=0)

class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(smallestLurch([3, 8, 1, 10, 4]), 4)
        self.assertEqual(smallestLurch([7, 2]), 5)
        self.assertEqual(smallestLurch([5, 5, 5]), 0)
        self.assertEqual(smallestLurch([9]), 0)
        self.assertEqual(smallestLurch([10, 0, 11]), 10)
        self.assertEqual(smallestLurch([0, 1, 2, 100]), 98)
        self.assertEqual(smallestLurch([0, 10, 20]), 10)
        self.assertEqual(smallestLurch([0, 1, 100]), 99)
        self.assertEqual(smallestLurch([0, 500, 1000]), 500)
        self.assertEqual(smallestLurch([42, 7, 19, 88, 3, 56, 71, 25, 94, 11, 63, 37, 50]), 17)

if __name__ == "__main__":
    unittest.main()
