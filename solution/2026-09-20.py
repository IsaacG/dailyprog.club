"""An Unhurried Tally

The heavens and the earth were finished, and all their host; and on the seventh day the Maker rested from all the work, and blessed the seventh day and made it holy.

The Man keeps the rhythm of that first week, six days of work and then a day of rest, and his first work is the tally of the host. `counts` lists the kinds of creature: `counts[i]` is how many creatures there are of kind i.
He counts according to its kind, one kind to a day.
Each day he counts up to `pace` creatures of a single kind and then leaves off until morning; if the kind is finished sooner he leaves off all the same, and takes up the next kind the next morning.
The days are numbered from 1, and every seventh day (the 7th, the 14th, and so on) is a day of rest on which he counts nothing.
There are always at least as many days of work as there are kinds.
Return the gentlest pace that will do: the smallest `pace` at which the whole host is counted by the end of day `days`.

Constraints: `1 <= n <= 500`, where `n` is the number of kinds in `counts`; `1 <= counts[i] <= 1000000000`; `1 <= days <= 10000`.
"""
import unittest
import itertools
import math

def gentlestPace(counts, days):
    """Return the smallest pace at which the whole host is counted by the end of day days."""
    workdays = lambda x: 6 * (x // 7) + (x % 7)
    total_days = lambda x: next(i for i in itertools.count(x) if workdays(i) == x)
    days_at_pace = lambda pace: total_days(sum(math.ceil(count / pace) for count in counts))
    lo, hi = 1, max(counts)
    while lo < hi:
        mid = (hi + lo) // 2
        if days_at_pace(mid) > days:
            lo = mid + 1
        else:
            hi = mid
    return hi



class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(gentlestPace([10, 4, 7, 12], 13), 4)
        self.assertEqual(gentlestPace([1000000], 7), 166667)
        self.assertEqual(gentlestPace([5, 9, 2], 3), 9)
        self.assertEqual(gentlestPace([1, 1, 1, 1, 1, 1], 6), 1)
        self.assertEqual(gentlestPace([1000000000, 1], 8), 166666667)

if __name__ == "__main__":
    unittest.main()
