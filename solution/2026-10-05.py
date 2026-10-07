"""The Overbooked Herb Beds

At the community garden, each planting bed is reserved as a stretch of days, and every reservation is given as a start day and an end day in two arrays, `starts` and `ends`.
The span for index i begins on day `starts[i]` and runs up to but not including day `ends[i]`, so a bed reserved from day 0 to day 4 is free again on day 4.
Two reservations that only touch, one ending on the very day the next begins, never share a day.
Return the total number of days that at least two reservations have booked at the same time.
A day booked by three or more reservations still counts only once.

### Constraints

* 0 <= the number of reservations <= 8
* every start day is an integer from 0 to 1000 inclusive
* every end day is an integer from 1 to 1000 inclusive
* each reservation's end day is strictly greater than its start day
"""
import unittest

def overlapLength(starts, ends):
    """Return the total length covered by at least two spans at once."""
    starts.sort(reverse=True)
    ends.sort(reverse=True)
    current_day, active_bookings, overlaps = 0, 0, 0
    while ends:
        while ends and ends[-1] <= current_day:
            active_bookings -= 1
            ends.pop()
        while starts and starts[-1] <= current_day:
            active_bookings += 1
            starts.pop()
        next_day = min(starts[-1], ends[-1]) if starts else ends[-1] if ends else 0
        if active_bookings > 1:
            overlaps += next_day - current_day
        current_day = next_day
    return overlaps



class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(overlapLength([1, 2, 7], [4, 6, 9]), 2)
        self.assertEqual(overlapLength([0, 1, 2], [5, 6, 7]), 5)
        self.assertEqual(overlapLength([0, 4], [4, 8]), 0)
        self.assertEqual(overlapLength([0, 1], [10, 5]), 4)
        self.assertEqual(overlapLength([0, 10], [3, 12]), 0)
        self.assertEqual(overlapLength([0, 1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14, 15]), 13)

if __name__ == "__main__":
    unittest.main()
