"""Balancing the Sample Tray

A lab bench holds a row of sample vials, each with a label and a recorded mass.
Before the run, one vial has to come off the tray so the rest can be split onto two pans of an equal-arm balance that come out level.
Given `labels`, the name of each vial, and `weights`, where `weights[i]` is the mass of vial i, return the labels of every vial whose removal leaves the remaining vials splittable into two sets of equal total mass (a set may be empty).
Sort the returned labels alphabetically.
If no vial works, return an empty array.

### Constraints

* `labels` and `weights` have the same length, from 1 to 30 vials
* each mass is an integer from 1 to 40
"""
import unittest

import collections
import functools

def removableForBalance(labels, weights):
    """Return the labels of items whose removal leaves two equal-total groups."""
    w2l = collections.defaultdict(set)
    for l, w in zip(labels, weights):
        w2l[w].add(l)

    out = set()
    weights = tuple(sorted(weights, reverse=True))
    return sorted({
        j
        for i, w in enumerate(weights)
        if canSplit(weights[:i] + weights[i + 1:], 0)
        for j in w2l[w]
    })


# 2026-07-17
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
        self.assertEqual(removableForBalance(["a", "b", "c", "d"], [1, 2, 3, 4]), ["b", "d"])
        self.assertEqual(removableForBalance(["only"], [7]), ["only"])
        self.assertEqual(removableForBalance(["a", "b", "c", "d"], [2, 2, 2, 2]), [])
        self.assertEqual(removableForBalance(["z", "y", "x", "w"], [1, 2, 3, 4]), ["w", "y"])
        self.assertEqual(removableForBalance(["a", "b", "c", "d", "e", "f"], [1, 4, 5, 6, 7, 8]), ["a", "c", "e"])
        self.assertEqual(removableForBalance(["a", "b", "c", "d", "e"], [1, 2, 3, 4, 5]), ["a", "c", "e"])
        self.assertEqual(removableForBalance(["a", "b", "c"], [1, 1, 2]), ["c"])
        self.assertEqual(removableForBalance(["a", "b"], [2, 4]), [])
        self.assertEqual(removableForBalance(["a", "b", "c"], [20, 20, 40]), ["c"])
        self.assertEqual(removableForBalance(["L01", "L02", "L03", "L04", "L05", "L06", "L07", "L08", "L09", "L10", "L11", "L12", "L13", "L14", "L15", "L16", "L17", "L18", "L19", "L20", "L21", "L22", "L23", "L24", "L25", "L26", "L27", "L28", "L29", "L30"], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]), ["L01", "L02", "L03", "L04", "L05", "L06", "L07", "L08", "L09", "L10", "L11", "L12", "L13", "L14", "L15", "L16", "L17", "L18", "L19", "L20", "L21", "L22", "L23", "L24", "L25", "L26", "L27", "L28", "L29"])

if __name__ == "__main__":
    unittest.main()
