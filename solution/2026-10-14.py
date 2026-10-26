"""The Longest Calm Spell at the Weather Station

A weather station logs the wind vane's bearing once per observation, and the dial is marked with twelve positions, numbered 0 through 11.
Between two readings that sit next to each other in the row, the vane swung forward by some number of marks: the count from the earlier reading to the later one, wrapping past 11 back to 0.
So 10 followed by 2 is a swing of 4 marks, and 10 followed by 0 is a swing of 2 marks.
A reading followed by the same reading is a swing of 0 marks.

A stretch of consecutive readings is calm when the swing is the same number of marks from every reading in the stretch to the next one.
A stretch may be as short as two readings, and such a stretch has only one swing, so it is always calm.

Among all calm stretches, the station wants the longest one.
If two or more calm stretches are equally long, it wants the one whose first reading comes first in the row.
Return that stretch as an object with exactly two fields: `lo`, the 0-based position of its first reading, and `hi`, the 0-based position of its last reading, inclusive.

### Constraints

* 2 <= the number of readings <= 15
* every reading is an integer from 0 to 11 inclusive
"""
import unittest
import itertools

def longestSteadyStretch(values):
    "Work out which stretch the story asks for, then set lo and hi to its first and last positions."""
    swings = [a - b if abs(a - b) <= 6 else (a - b) + (-12 if a > b else +12) for a, b in itertools.pairwise(values)]
    lo, hi = 0, 0
    for _, b in itertools.groupby(enumerate(swings), key=lambda x: x[1]):
        b = list(b)
        if len(b) > hi - lo + 1:
            lo, hi = b[0][0], b[-1][0]

    return {"lo": lo, "hi": hi + 1}

class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(longestSteadyStretch([9, 11, 1, 3, 6]), {"lo": 0, "hi": 3})
        self.assertEqual(longestSteadyStretch([1, 2, 3, 0, 1, 2]), {"lo": 0, "hi": 2})
        self.assertEqual(longestSteadyStretch([4, 4, 4]), {"lo": 0, "hi": 2})
        self.assertEqual(longestSteadyStretch([10, 0, 2, 4]), {"lo": 0, "hi": 3})
        self.assertEqual(longestSteadyStretch([8, 2]), {"lo": 0, "hi": 1})
        self.assertEqual(longestSteadyStretch([3, 8, 3, 8]), {"lo": 0, "hi": 1})
        self.assertEqual(longestSteadyStretch([0, 3, 6, 7, 8, 9]), {"lo": 2, "hi": 5})
        self.assertEqual(longestSteadyStretch([5, 0, 7, 2, 9, 4, 11, 6, 10, 2, 6, 10, 2, 6, 10]), {"lo": 0, "hi": 7})

if __name__ == "__main__":
    unittest.main()
