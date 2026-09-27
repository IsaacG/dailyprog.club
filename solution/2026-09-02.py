"""The Lantern Ribbon

At the harvest festival, a string of paper lanterns hangs between two poles.
Each lantern carries a painted number.
The list `candles` holds those numbers from left to right, and `candles[i]` is the number painted on the i-th lantern.

Two children, Mira and Theo, stand at the two ends with a long ribbon.
Mira holds the left end of the ribbon at the leftmost lantern, and Theo holds the right end at the rightmost lantern.
Each round they compare the two lanterns they are holding.

### One round

* If the two painted numbers are both odd or both even, the lanterns match.
  The children tie one ribbon knot between them, then both step inward: Mira moves one lantern to the right, Theo moves one lantern to the left.
* Otherwise, one number is odd and the other even.
  They tie no knot.
  The child holding the smaller number steps one lantern inward (Mira to the right if her lantern is smaller, Theo to the left if his is smaller); the other child stays put.
  In this case the two numbers can never be equal, so there is never a tie about who steps.

The rounds continue only while Mira's lantern is somewhere to the left of Theo's lantern.
When they reach the same lantern, or pass each other, the rounds stop.

### Return

Return an object with three fields:

* `answer`: how many ribbon knots were tied.
* `lo`: Mira's position at the start of each round, in order, starting with the first round.
* `hi`: Theo's position at the start of each round, in the same order.

Lantern positions are counted from 0, so the leftmost lantern is position 0.

Constraint: `n` is the number of lanterns, with 2 <= n <= 15.
Each `candles[i]` is a whole number between 1 and 100.
"""
import unittest

def ribbonKnots(candles):
    l, r = 0, len(candles) - 1
    lo, hi = [], []
    knots = 0
    while l < r:
        lo.append(l)
        hi.append(r)
        if candles[l] % 2 == candles[r] % 2:
            knots += 1
            l += 1
            r -= 1
        elif candles[l] < candles[r]:
            l += 1
        else:
            r -= 1
    return {"answer": knots, "lo": lo, "hi": hi}

class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(ribbonKnots([2, 7, 4, 5]), {"answer": 1, "lo": [0, 1], "hi": [3, 3]})
        self.assertEqual(ribbonKnots([2, 4, 6, 8, 10]), {"answer": 2, "lo": [0, 1], "hi": [4, 3]})
        self.assertEqual(ribbonKnots([1, 2]), {"answer": 0, "lo": [0], "hi": [1]})

if __name__ == "__main__":
    unittest.main()
