"""Booking the Reading Room

The archive keeps a single reading room for its rare manuscripts and lets visiting scholars book it, each request covering a stretch of the day from a start hour to an end hour.
Two requests can share the day as long as their stretches never overlap; a request that ends exactly as another begins is fine.

Given `starts` and `ends`, where request i runs from `starts[i]` to `ends[i]`, choose the set of requests that fills the most total time across the day.
If several sets fill the same total time, prefer the one with more requests; if those also match in number, prefer the one whose requests come earlier in the given list, comparing request numbers in ascending order at the first place they differ.

Return an object with a single field `keep`, holding the numbers of the chosen requests in ascending order.

### Constraints

* `starts` and `ends` have the same length, from 1 to 8 requests
* every start hour and every end hour is an integer from 0 to 24 inclusive
"""
import unittest

def bestBookings(starts, ends):
    """Work out which intervals the story asks for, then append their indices in ascending order."""
    pairs = [(start, end, idx) for idx, (start, end) in enumerate(zip(starts, ends))]
    pairs.sort()
    duration = {idx: end - start for start, end, idx in pairs}
    n = len(pairs)
    sort_key = lambda x: (-sum(duration[i] for i in x), -len(x), min(x, default=[]))

    def best(idx, free):
        if idx == n:
            return []
        options = [best(idx + 1, free)]
        if pairs[idx][0] >= free:
            options.append([pairs[idx][2]] + best(idx + 1, pairs[idx][1]))
        return min(options, key=sort_key)

    return {"keep": sorted(best(0, 0))}


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(bestBookings([0, 5, 2, 12], [3, 9, 6, 15]), {"keep": [0, 1, 3]})
        self.assertEqual(bestBookings([0, 0, 5], [10, 4, 10]), {"keep": [0]})
        self.assertEqual(bestBookings([0, 12], [12, 24]), {"keep": [0, 1]})
        self.assertEqual(bestBookings([0, 0, 3], [6, 3, 6]), {"keep": [1, 2]})
        self.assertEqual(bestBookings([0, 0, 2, 5], [3, 2, 6, 8]), {"keep": [0, 3]})
        self.assertEqual(bestBookings([2, 2, 2], [6, 6, 6]), {"keep": [0]})
        self.assertEqual(bestBookings([5], [12]), {"keep": [0]})
        self.assertEqual(bestBookings([0, 1, 2, 3, 4, 5, 6, 7], [2, 3, 4, 5, 6, 7, 8, 9]), {"keep": [0, 2, 4, 6]})

if __name__ == "__main__":
    unittest.main()
