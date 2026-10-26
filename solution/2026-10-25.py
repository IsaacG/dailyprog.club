"""Extras on the Tab

A restaurant's extras ledger records only the total charge for extras on each order.

You are given `extras`, an ordered list of distinct extra names, and `totals`, a list of recorded charges.
The extra at index `i` costs 2^i coins, with indices starting at 0.
Each recorded charge is the sum of the prices of its selected extras, each selected at most once, and uses only extras in the supplied list.

Return the names of all extras selected on at least one order, in their original list order and without duplicates.
A zero charge includes no extras, and an empty ledger produces an empty result.

### Constraints

* The number of names in `extras` is from 1 to 8 inclusive.
* The number of charges in `totals` is from 0 to 64 inclusive.
* Each charge is an integer from 0 to 255 inclusive.
* Extra names are distinct, nonempty lowercase ASCII strings.
"""
import unittest

def collectExtras(extras, totals):
    """Return the included extras in their original order."""
    bits = 0
    for t in totals:
        bits |= t
    return [extra for i, extra in enumerate(extras) if bits & (1 << i)]

class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(collectExtras(["ki", "ab", "zo", "de", "mu", "pa"], [3, 8, 16]), ["ki", "ab", "de", "mu"])
        self.assertEqual(collectExtras(["aa", "bb", "cc"], [1, 1]), ["aa"])
        self.assertEqual(collectExtras(["aa", "bb", "cc"], [5]), ["aa", "cc"])
        self.assertEqual(collectExtras(["aa"], []), [])
        self.assertEqual(collectExtras(["aa", "bb"], [0, 0]), [])
        self.assertEqual(collectExtras(["aa", "bb", "cc", "dd"], [8, 0]), ["dd"])
        self.assertEqual(collectExtras(["aa", "bb", "cc", "dd", "ee", "ff", "gg", "hh"], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]), ["aa", "bb", "cc", "dd", "ee", "ff", "gg", "hh"])

if __name__ == "__main__":
    unittest.main()
