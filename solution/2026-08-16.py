"""The Berry Stall

A market stall posts a berry price every morning of the fair.
The array `prices` lists the price of one basket for each day in order, so `prices[i]` is the price on day i.
You may buy a basket on the morning of some day and sell it on the morning of any later day.
Return the largest profit you can make, or 0 if no later day is dearer than an earlier day.

Constraints: 1 <= n <= 100, where `n` is the number of days in `prices`; each price is an integer from 0 to 1000.
"""
import unittest

def bestProfit(prices):
    """Return the largest profit from buying on one day and selling on a later day, or 0."""
    best = 0
    if not prices:
        return 0
    lowest = prices[0]
    for price in prices[1:]:
        best = max(best, price - lowest)
        lowest = min(lowest, price)
    return best



class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(bestProfit([3, 5, 7, 9]), 6)
        self.assertEqual(bestProfit([4, 6, 2, 8]), 6)
        self.assertEqual(bestProfit([5, 5, 5]), 0)

if __name__ == "__main__":
    unittest.main()
