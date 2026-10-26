"""Two Matching Rounds at the Firing Range

At the firing range, each shot's score is listed in `values`, and the range officer wants to know whether the day's card contains two separate rounds that each add up to `target`.
Each round uses exactly two shots, the two rounds share no shot, and the order of shots within a round does not matter.
Return `true` if such a split of four distinct shots into two target-scoring rounds exists, and `false` otherwise.

### Constraints

* The number of shots is from 0 to 50.
* Each shot's score is an integer from -50 to 50.
* `target` is an integer from -100 to 100.
"""
import unittest
import itertools

def twoMatchingRounds(values, target):
    """Return True if two disjoint pairs of distinct indices each sum to target."""
    return any(
        sum(group) == 2 * target and any(i == target - group[0] for i in group[1:])
        for group in itertools.combinations(values, r=4)
    )


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(twoMatchingRounds([1, 2, 3, 4], 5), True)
        self.assertEqual(twoMatchingRounds([-1, 1, 2, -2], 0), True)
        self.assertEqual(twoMatchingRounds([-1, -2, -3, -4], -5), True)
        self.assertEqual(twoMatchingRounds([0, 0, 0, 1], 0), False)
        self.assertEqual(twoMatchingRounds([1, 1, 1, 7], 5), False)
        self.assertEqual(twoMatchingRounds([1, 2, 3, 4], 10), False)
        self.assertEqual(twoMatchingRounds([3, 1, 5], 6), False)
        self.assertEqual(twoMatchingRounds([2, 2, 2, 2], 4), True)
        self.assertEqual(twoMatchingRounds([], 0), False)
        self.assertEqual(twoMatchingRounds([7], 14), False)
        self.assertEqual(twoMatchingRounds([5, 5], 10), False)
        self.assertEqual(twoMatchingRounds([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 2), True)

if __name__ == "__main__":
    unittest.main()
