"""The Two-Bag Job

Two porters are walking the loot away from a job, one duffel bag each.
They are paid by the piece, so the two bags have to end up holding the same number of pieces: exactly half the pieces each, with every piece going in one bag or the other.
The number of pieces is even.

The array `weights` holds the weights of the pieces, where `weights[i]` is the weight of piece i.
Decide which pieces go in which bag so the two bags weigh as nearly the same as possible, and return the smallest achievable difference between the two total weights.

### Constraints

* The number of pieces is even, at least 2 and at most 32.
* Each piece weighs between 1 and 1000000.
"""
import time
import unittest

import functools
import itertools

def twoBagJob(weights):
    """Return the smallest difference in total weight between two equal-sized loads."""
    diffs = sorted(a - b for a, b in itertools.batched(sorted(weights, reverse=True), 2))
    num = len(diffs)

    # Based on 2026-07-17
    # @functools.cache
    def min_diff(idx, balance):
        if idx == num:
            return balance
        # remaining = sum(diffs[idx:])
        # if remaining == balance:
        #     return 0
        # if remaining < balance:
        #     return balance - remaining
        return min(
            min_diff(idx + 1, balance + diffs[idx]),
            min_diff(idx + 1, abs(balance - diffs[idx])),
        )

    return min_diff(0, 0)

class TestSolution(unittest.TestCase):
    def test_data(self):
        start = time.time()
        self.assertEqual(twoBagJob([6, 5, 4, 3, 2, 1]), 1)
        self.assertEqual(twoBagJob([10, 8, 6, 4]), 0)
        self.assertEqual(twoBagJob([9, 2, 2, 2, 2, 2]), 7)
        self.assertEqual(twoBagJob([9, 4]), 5)
        end = time.time()
        print((end - start) * 1000000)

if __name__ == "__main__":
    unittest.main()
