"""The Potter's Test Strip

At the pottery, cups are set out in a row on the shelf before firing.
Each cup's glaze is recorded in the list `glazes`, and `glazes[i]` is the number of the glaze on cup i, with every glaze numbered 0, 1, 2, or 3.

The master wants to pick one contiguous run of at least two cups as a test strip.
The cup at the left end and the cup at the right end of the run must carry the same glaze, and no cup between those two ends may carry that glaze.
She wants the longest run she can get.
If two runs are tied for longest, she takes the one closer to the west end of the shelf.

Return the positions of the first and last cup of that run, as an object with fields `lo` and `hi`.

Constraint: `n` is the number of cups, with 2 <= n <= 8.
Each `glazes[i]` is 0, 1, 2, or 3.
The shelf always holds at least two cups with the same glaze, so such a run always exists.
"""
import unittest

def glazeRun(glazes):
    """Work out which run the story asks for, then set lo and hi to its first and last positions."""
    lo, hi = 0, 0
    best = 0
    last = {}
    for i, glaze in enumerate(glazes):
        if (run := i - last.get(glaze, i)) > best:
            best, hi, lo = run, i, last[glaze]
        last[glaze] = i

    return {"lo": lo, "hi": hi}


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(glazeRun([0, 1, 2, 3, 0, 1, 2, 3]), {"lo": 0, "hi": 4})
        self.assertEqual(glazeRun([1, 0, 2, 1, 3, 0]), {"lo": 1, "hi": 5})
        self.assertEqual(glazeRun([2, 2]), {"lo": 0, "hi": 1})

if __name__ == "__main__":
    unittest.main()
