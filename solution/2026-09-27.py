"""Hilltop Ring of Stones

A ring of standing stones circles a hilltop, and each stone has a target height.
You can raise any run of neighboring stones around the ring by one unit per day, but no stone may ever stand taller than its target.
All stones start at ground level.

Given `heights`, an array where `heights[i]` is the target height of stone i, return the fewest days needed to bring every stone to exactly its target height.

### Constraints

* 1 <= number of stones <= 9000
* 0 <= each target height <= 50
* A stone with target height 0 is already finished.
"""
import unittest

def countStrokes(heights):
    """Return the fewest operations needed to reach the required heights."""
    length = len(heights)
    answer = 0
    while any(heights):
        idx = heights.index(min(h for h in heights if h))
        for forward in range(length):
            if heights[(idx + forward + 1) % length] < heights[(idx + forward) % length]:
                break
        for backward in range(length - forward):
            if heights[(idx - backward - 1) % length] < heights[(idx - backward) % length]:
                break
        for j in range(idx - backward, idx + forward + 1):
            heights[j % length] -= 1
        answer += 1
    return answer




class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(countStrokes([1, 3, 2]), 3)
        self.assertEqual(countStrokes([3, 2, 2, 3]), 3)
        self.assertEqual(countStrokes([1, 2, 1, 2]), 2)
        self.assertEqual(countStrokes([1, 3, 1, 3]), 4)
        self.assertEqual(countStrokes([7]), 7)
        self.assertEqual(countStrokes([4, 4, 4, 4]), 4)

if __name__ == "__main__":
    unittest.main()
