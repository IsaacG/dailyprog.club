"""Expedition Supplies

You're leading a research expedition.
Your vehicle has a weight capacity, and each piece of gear has a weight (kg) and a survival value (importance rating).
Choose a subset of items to maximize total survival value without exceeding the weight limit.
You cannot take fractional items.
Given an array `items` where each item is [weight, value], and an integer `capacity`, return the maximum total value achievable.
"""
import unittest
import functools

def expeditionSupplies(items, capacity):
    """Return max value without exceeding capacity."""

    @functools.cache
    def solve(capacity, items):
        return max(
            (
                solve(capacity - items[i][0], items[:i] + items[i + 1:]) + items[i][1]
                for i in range(len(items))
                if items[i][0] <= capacity
            ),
            default=0,
        )

    return solve(capacity, tuple(sorted(tuple(i) for i in items)))


class TestSolution(unittest.TestCase):
    def test_data(self):
        # self.assertEqual(expeditionSupplies([[2, 10], [3, 15], [5, 40]], 7), 50)
        self.assertEqual(expeditionSupplies([[1, 1], [2, 2], [3, 3]], 10), 6)
        self.assertEqual(expeditionSupplies([[5, 100]], 5), 100)
        self.assertEqual(expeditionSupplies([[10, 60], [20, 100], [30, 120]], 50), 220)
        self.assertEqual(expeditionSupplies([], 10), 0)
        self.assertEqual(expeditionSupplies([[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], 15), 15)

if __name__ == "__main__":
    unittest.main()
