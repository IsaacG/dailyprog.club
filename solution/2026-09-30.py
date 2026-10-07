"""The Relay Carnival Baton Order

A carnival relay team hands off a single baton around the track, and each runner's leg is logged as a start and an end moment.
The legs are given by two arrays of the same length, `starts` and `ends`: leg i begins at `starts[i]` and finishes at `ends[i]`, with `starts[i]` never later than `ends[i]`.
A run is a set of distinct legs that can be lined up one after another so each leg's finish moment is exactly the next leg's start moment, with no overlap and no idle gap between them; a run may also be just one leg.
The carnival wants the longest run the team could have strung together, and if several runs tie for length, the one that uses the earliest-logged leg wins; if they share that leg, the earliest-logged leg they do not share decides.
Return an object with a single field `keep` holding the leg numbers in that run, listed in the order the legs were given, smallest number first.

### Constraints

* `starts` and `ends` hold between 1 and 8 legs each, and always the same number of legs.
* Every start and end moment is an integer from 0 to 30 inclusive.
* `starts[i]` is never later than `ends[i]`.
"""
import unittest

def longestChain(starts, ends):
    sort_key = lambda x: (-x[0], x[1])

    def best_run(i: int) -> tuple[int, tuple[int, ...]]:
        options = [best_run(j) for j, start in enumerate(starts) if start == ends[i]]
        if not options:
            return 1, (i,)
        size, legs = sorted(options, key=sort_key)[0]
        return 1 + size, (i,) + legs

    options = [best_run(i) for i in range(len(starts))]
    runs = min(options, key=sort_key, default=(0, ()))[1]
    return {"keep": sorted(runs)}

class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(longestChain([2, 0, 6, 4, 8], [6, 2, 9, 5, 10]), {"keep": [0, 1, 2]})
        self.assertEqual(longestChain([2], [7]), {"keep": [0]})
        self.assertEqual(longestChain([0, 5, 5, 6, 7, 8], [5, 6, 7, 20, 8, 9]), {"keep": [0, 2, 4, 5]})
        self.assertEqual(longestChain([0, 1], [5, 6]), {"keep": [0]})
        self.assertEqual(longestChain([0, 3, 7], [2, 5, 9]), {"keep": [0]})
        self.assertEqual(longestChain([0, 5, 6, 7], [10, 6, 7, 8]), {"keep": [1, 2, 3]})
        self.assertEqual(longestChain([10, 12, 0, 5], [12, 14, 5, 7]), {"keep": [0, 1]})
        self.assertEqual(longestChain([0, 4, 4, 8, 8, 12, 2, 20], [4, 8, 10, 12, 15, 16, 3, 25]), {"keep": [0, 1, 3, 5]})

if __name__ == "__main__":
    unittest.main()
