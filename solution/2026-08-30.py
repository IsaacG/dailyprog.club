"""The Cloakroom Mix-Up

After the final encore, the whole audience crowds the cloakroom at once.
The attendant has `n` guests and `n` coats, and in the rush it is impossible to tell which coat belongs to whom.
The one rule that keeps the evening from ending in chaos: no guest may be handed their own coat.

Count the number of ways the attendant can hand out all `n` coats, one to each guest, so that no guest receives their own coat.
Two handouts are different when at least one guest receives a different coat.

Constraints: `1 <= n <= 12`.
"""
import unittest
import functools

def countMixUps(n):
    """Count the ways to hand back coats so nobody gets their own coat."""
    return count(n - 1, frozenset(range(n)))

@functools.cache
def count(n, available):
    if n == 0:
        if n in available:
            return 0
        return 1
    i = 0
    for j in available:
        if j != n:
            i += count(n - 1, frozenset(available - {j}))
    return i


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(countMixUps(3), 2)
        # self.assertEqual(countMixUps(4), 9)
        # self.assertEqual(countMixUps(5), 44)

if __name__ == "__main__":
    unittest.main()
