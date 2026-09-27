"""Where the New Moon Falls

The Maker set two great lights in the expanse of the sky, the greater to rule the day and the lesser to rule the night, and the stars also, for signs and for seasons, for days and for years; and there was evening and there was morning, the fourth day.

The lesser light marks out the months.
A month begins on the night of a new moon and, according to its kind, lasts 29 or 30 nights; the night after its last is the next new moon.
A year is made of whole months laid end to end: it begins with a new moon on its first night, and the night after its last night is a new moon again.
A year is `nights` nights long, its nights numbered from 1, and there may be several ways to make it up from months.
Return the number of nights on which a new moon falls in at least one of those ways, or 0 if no way of laying out whole months fills the year exactly.

Constraints: `1 <= nights <= 1000`.
"""
import unittest
import functools

def newMoonNights(nights):
    """Return how many nights of the year can carry a new moon in some layout of whole months."""
    ways = set()
    
    @functools.cache
    def solve(nights):
        if nights >= 29 and any([nights <= 30, solve(nights - 29), solve(nights - 30)]):
            ways.add(nights)
            return True
        return False

    solve(nights)
    return len(ways)


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(newMoonNights(354), 48)
        self.assertEqual(newMoonNights(59), 3)
        self.assertEqual(newMoonNights(61), 0)

if __name__ == "__main__":
    unittest.main()
