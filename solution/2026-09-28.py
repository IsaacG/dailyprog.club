"""The Ledger of Long Numbers

A clerk keeps a ledger of tallies.
Each tally is a run of digits with no leading zero, and the clerk must write every tally into one long entry, using each tally exactly once, in any order.

The ledger's `parts` is a list of those tallies, where `parts[i]` is the i-th tally as a string of digits.
Return the largest number that can be written by joining all the tallies in some order, as a string.

### Constraints

* `parts` has between 1 and 100 tallies.
* Each tally is between 1 and 9 digits long.
* No tally begins with '0'.
"""
import unittest
import functools


def largestJoin(parts):
    """Return the largest number formed by joining every part once, as a string."""
    return "".join(sorted(parts, key=functools.cmp_to_key(lambda a, b: int(a + b) - int(b + a)), reverse=True))


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(largestJoin(["5", "61", "2"]), "6152")
        self.assertEqual(largestJoin(["3", "30", "34", "5", "9"]), "9534330")
        self.assertEqual(largestJoin(["3", "34"]), "343")
        self.assertEqual(largestJoin(["9", "10"]), "910")
        self.assertEqual(largestJoin(["42"]), "42")
        self.assertEqual(largestJoin(["30", "3", "989", "12", "98", "34", "121", "5", "9", "1", "100", "10"]), "99899853433012121110100")

if __name__ == "__main__":
    unittest.main()
