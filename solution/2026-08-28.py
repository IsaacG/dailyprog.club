"""The Paved Mile

The highway department is walking a long street segment by segment.
The array `road` describes the pavement: `road[i]` is 1 if segment i is already smooth, and 0 if it has a pothole.
A crew can patch at most `k` potholes, and they will spend the day on one continuous stretch of the street.
After patching, every segment in the stretch must be smooth.

Return the number of segments in the longest continuous stretch that can be made smooth by patching at most `k` potholes.

### Constraints

* `n` is the length of `road`, with 0 <= n <= 9998.
* Each `road[i]` is 0 or 1.
* `k` is between 0 and `n`, inclusive.
"""
import unittest

def longestSmoothRun(road, k):
    """Return the longest stretch that can be smoothed with at most k patches."""
    def start(i):
        allowed = k
        for j, r in enumerate(road[i:]):
            if r == 0:
                if allowed == 0:
                    return j
                allowed -= 1
        return len(road[i:])

    if not road:
        return 0
    return max(start(i) for i in range(len(road)))

# A more efficient O(2n) solution can be done with a pair of pointers.


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(longestSmoothRun([1, 0, 1, 1, 0, 1], 1), 4)
        self.assertEqual(longestSmoothRun([1, 1, 1], 1), 3)
        self.assertEqual(longestSmoothRun([0, 0, 0, 0], 1), 1)

if __name__ == "__main__":
    unittest.main()
