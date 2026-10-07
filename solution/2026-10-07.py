"""One Lamp Down the Hall

A row of guest rooms each leave a small panel of four lamps lit or dark, and the housekeeper logs each room as a single number from 1 to 15.
Read the number in binary: lamp k is lit exactly when bit k is 1, counting from bit 0, so 5 means lamps 0 and 2 are lit.

She wants the longest unbroken run of rooms she can describe with one shared lamp: some lamp that is lit in every room of the run.
Return that run as an object with fields `lo` and `hi`, the 0-based positions of the first and last room in it.
If two runs are equally long, choose the one whose first room comes first.

### Constraints

* `values` has between 2 and 15 numbers
* every number in `values` is between 1 and 15 inclusive
"""
import unittest

def longestCommonFlagRun(values):
    """Work out which stretch the story asks for, then set lo and hi to its first and last positions."""
    start = [None] * 4
    best_len, best_pair = 0, (0, 0)
    for idx, value in enumerate(values):
        for i in range(4):
            if 1 << i & value:
                if start[i] is None:
                    start[i] = idx
                elif idx - start[i] > best_len:
                    best_len = idx - start[i]
                    best_pair = (start[i], idx)
            else:
                start[i] = None
    lo, hi = best_pair
    return {"lo": lo, "hi": hi}


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(longestCommonFlagRun([6, 4, 5, 2, 3, 1]), {"lo": 0, "hi": 2})
        self.assertEqual(longestCommonFlagRun([5, 10]), {"lo": 0, "hi": 0})
        self.assertEqual(longestCommonFlagRun([3, 5, 6]), {"lo": 0, "hi": 1})
        self.assertEqual(longestCommonFlagRun([1, 3, 6, 6, 6]), {"lo": 1, "hi": 4})
        self.assertEqual(longestCommonFlagRun([3, 3, 5, 4, 6]), {"lo": 0, "hi": 2})
        self.assertEqual(longestCommonFlagRun([4, 5, 3, 6, 2, 10]), {"lo": 2, "hi": 5})
        self.assertEqual(longestCommonFlagRun([7, 1, 6, 2, 5, 4, 3, 1, 2, 9, 12, 10, 8, 9, 6]), {"lo": 9, "hi": 13})

if __name__ == "__main__":
    unittest.main()
