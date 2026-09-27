"""Burrow Watch

On a windswept island, petrels nest in a branching burrow system.
A chick is watched when a sensor sits in its own chamber or in any chamber joined to it by one tunnel.
Each tunnel has two ends, so a sensor watches both ends of every tunnel it touches.

`cost` has length n, where n is the number of chambers. `left` and `right` each have length n-1: for every i below n-1, `left[i]` and `right[i]` give the two onward tunnels from chamber i, or -1 when no such tunnel exists.
Every tunnel leads to a higher-numbered chamber, and from chamber 0 there is exactly one route to every chamber.
Placing a sensor in chamber i costs `cost[i]`.
Return the smallest total cost for which every chamber is watched.

Constraints: `1 <= n <= 100`, where `n` is the number of chambers.
Each `cost[i]` is an integer in `[0, 1000000]`, and each `left[i]` or `right[i]` is either `-1` or an integer in `[0, n-1]`.
"""
import unittest
import functools

def minSensorCost(cost: list[int], left: list[int], right: list[int]) -> int:
    """Return the smallest total cost that watches every chamber."""
    childrens = [[j for j in (left[i], right[i]) if j != -1] for i in range(len(cost) - 1)] + [[]]

    @functools.cache
    def solve(i: int, watched: bool) -> int:
        """Recursively solve the cost to watch i and onwards.

        If the prior chamber has a sensor, this chamber is already watched.
        """
        children = childrens[i]
        if not children:
            if watched:
                return 0
            return cost[i]
        options = []
        # Install a sensor in this chamber.
        options.append(cost[i] + sum(solve(c, True) for c in children))
        # Install a sensor in one of the next chambers.
        if len(children) == 1:
            child = children[0]
            options.append(cost[child] + sum(solve(c, True) for c in childrens[child]))
        if len(children) == 2:
            for a, b in (children, reversed(children)):
                options.append(cost[a] + sum(solve(c, True) for c in childrens[a]) + solve(b, False))
        # If this chamber is watched, we may not need a sensor here at all.
        if watched:
            options.append(sum(solve(c, False) for c in children))
        return min(options)

    if len(cost) == 1:
        return cost[0]
    return solve(0, False)



class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(minSensorCost([9, 2], [1], [-1]), 2)
        self.assertEqual(minSensorCost([50, 1, 50], [1, 2], [-1, -1]), 1)
        self.assertEqual(minSensorCost([100, 2, 3], [1, -1], [2, -1]), 5)
        self.assertEqual(minSensorCost([100, 1, 100, 1], [1, 2, 3], [-1, -1, -1]), 2)
        self.assertEqual(minSensorCost([7], [], []), 7)
        self.assertEqual(minSensorCost([10, 100, 1, 1], [1, 2, -1], [-1, 3, -1]), 12)
        self.assertEqual(minSensorCost([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]), 34)
        self.assertEqual(minSensorCost([40, 3, 60, 0, 25, 7, 90, 12, 1, 0, 33, 5, 8, 2, 50], [1, 3, 5, 7, -1, 9, 11, -1, -1, 13, -1, -1, -1, -1], [2, 4, 6, 8, -1, 10, 12, -1, -1, 14, -1, -1, -1, -1]), 23)

if __name__ == "__main__":
    unittest.main()
