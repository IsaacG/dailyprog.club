"""Pirates' Fair Split

Two rival pirate crews discover a chest of gold coins, each with a positive integer value.
To avoid bloodshed, they agree to split the coins such that each crew gets exactly half the total value.
Can they do it? Given an array of coin values, return true if a fair split is possible, and false otherwise.
"""
import unittest
import functools

def fairSplitPirates(coins):
    """Return True if coins can be split evenly, False otherwise."""
    return canSplit(tuple(sorted(coins, reverse=True)), 0)

@functools.cache
def canSplit(coins, balance):
    if sum(coins) == balance:
        return True
    biggest, *rest = coins
    if len(rest) == 0:
        return biggest == balance
    if biggest > sum(rest) + balance:
        return False
    return canSplit(tuple(rest), abs(biggest + balance)) or canSplit(tuple(rest), abs(biggest - balance))


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(fairSplitPirates([1, 5, 11, 5]), True)
        self.assertEqual(fairSplitPirates([1, 2, 3, 5]), False)
        self.assertEqual(fairSplitPirates([2, 2]), True)
        self.assertEqual(fairSplitPirates([1]), False)
        self.assertEqual(fairSplitPirates([100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]), True)
        self.assertEqual(fairSplitPirates([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1000]), False)
        self.assertEqual(fairSplitPirates([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]), False)

if __name__ == "__main__":
    unittest.main()
