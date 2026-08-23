"""Loading the Harbor Ferry

A small harbor ferry carries vehicles across the channel.
Each vehicle in `weights` has a weight, and `weights[i]` is the weight of vehicle i.
The deck has two lanes, so a crossing can take two vehicles, but only when their combined weight is at most `limit`.
Each vehicle can be used in at most one crossing, and the ferry master may pair the vehicles in any order.
Return the largest number of two-vehicle crossings the ferry can make.

Constraints: `n` is the length of `weights`, with 0 <= n <= 200.
Each weight is an integer from 1 to 500, and `limit` is an integer from 1 to 1000.
"""
import unittest

def ferryTrips(weights, limit):
    """Return the largest number of two-vehicle crossings, or 0."""
    lo, hi = 0, len(weights) - 1
    total = 0

    while lo < hi:
        if weights[lo] + weights[hi] <= limit:
            lo += 1
            total += 1
        hi -= 1
    return total


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(ferryTrips([4, 4, 4, 4, 4, 4], 8), 3)
        self.assertEqual(ferryTrips([1, 2, 3], 3), 1)
        self.assertEqual(ferryTrips([2, 2, 9, 9], 4), 1)

if __name__ == "__main__":
    unittest.main()
