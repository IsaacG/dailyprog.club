"""The Symmetry Appraisal

A gemologist lays a tray of cut stones on the bench and wants to know whether they can be shown as matched pairs of equal weight, with every stone on the tray used exactly once.

Given `values`, an array of stone weights, return `true` if the stones can be divided into pairs so that each stone belongs to exactly one pair and every pair weighs the same, and `false` otherwise.
A tray with no stones on it counts as matched.

### Constraints

* The number of stones is between 0 and 24 inclusive.
* Each stone weight is an integer from 1 to 1000 inclusive.
"""
import unittest

def canPairEvenly(values):
    """Return True if every value can be paired off so all pairs share one total."""
    n = len(values)
    values.sort()
    return n % 2 == 0 and len({i + j for i, j in zip(values[:n // 2], reversed(values[n // 2:]))}) <= 1


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(canPairEvenly([1, 2, 3, 4]), True)
        self.assertEqual(canPairEvenly([1, 2, 3]), False)
        self.assertEqual(canPairEvenly([1, 1, 1, 3]), False)
        self.assertEqual(canPairEvenly([1, 2, 2, 5]), False)
        self.assertEqual(canPairEvenly([]), True)
        self.assertEqual(canPairEvenly([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 30]), False)

if __name__ == "__main__":
    unittest.main()
