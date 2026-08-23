"""The Shock Wave

An asteroid miner is sweeping a chain of `n` ore rocks in order.
The array `ore` lists the tonnage of each rock, so `ore[i]` is the tons of ore on rock `i`.
When the drone mines rock `i`, the shock wave cracks rock `i+1`, so rock `i+1` is unsalvageable by the time the sweep reaches it.
The drone may skip any rocks it likes.
Return the largest number of tons it can collect from the chain.

Constraints: `0 <= n <= 30`, where `n` is the length of `ore`, and each `ore[i]` is between 1 and 1000.
"""
import unittest

def maxOre(ore):
    """Return the largest tonnage collectable from the chain."""
    a, b = 0, 0
    for i in reversed(ore):
        a, b = max(a, i + b), a
    return max(a, b)


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(maxOre([5, 1, 1, 5]), 10)
        self.assertEqual(maxOre([2, 7, 3]), 7)
        self.assertEqual(maxOre([9]), 9)

if __name__ == "__main__":
    unittest.main()
