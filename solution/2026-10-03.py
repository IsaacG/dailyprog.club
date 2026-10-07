"""The Cargo Weigh-In

A freight office has a stack of crates on the dock, each stamped with its weight in whole kilograms, and a truck that cannot carry more than its rated capacity.
Given `weights`, an array of strings where `weights[i]` is the weight printed on crate i, and a whole number `capacity`, return the heaviest total load that can be placed on the truck without going over capacity.
Every crate is either loaded whole or left on the dock.
Crates that happen to share the same printed weight are separate crates, and each can be loaded at most once.
Loading nothing is allowed, so the answer is never negative.

### Constraints

* 2 <= the number of weights <= 32
* 0 <= `capacity` <= 1500000000
* every weight is a whole number from 1 to 100000000 inclusive
"""
import unittest
import functools

def bestTotalWithin(weights, capacity):
    """Return the largest total that does not exceed the capacity."""
    weights = sorted([int(i) for i in weights], reverse=True)
    n = len(weights)
    
    @functools.cache
    def solve(idx, capacity):
        if idx >= n:
            return 0
        weight = weights[idx]
        return max(solve(idx + 1, capacity), solve(idx + 1, capacity - weight) + weight if weight <= capacity else 0)

    return solve(0, capacity)


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(bestTotalWithin(["4", "7", "2", "9", "5", "3"], 18), 18)
        self.assertEqual(bestTotalWithin(["6", "9", "4", "7", "5", "8"], 20), 20)
        self.assertEqual(bestTotalWithin(["5", "5", "5"], 11), 10)
        self.assertEqual(bestTotalWithin(["8", "12"], 5), 0)
        self.assertEqual(bestTotalWithin(["30000000", "30000000", "30000000", "30000000", "30000000", "30000000", "30000000", "30000000", "30000000", "30000000", "30000000", "30000000", "30000000", "30000000", "30000000", "30000000", "70000000", "70000000", "70000000", "70000000", "70000000", "70000000", "70000000", "70000000", "70000000", "70000000", "70000000", "70000000", "70000000", "70000000", "70000000", "70000000"], 1000000000), 1000000000)
        self.assertEqual(bestTotalWithin(["2", "8", "3"], 7), 5)

if __name__ == "__main__":
    unittest.main()
