"""The Merchant's Tally

At the stone market, a merchant scratches each price onto a tag using ledger marks.
Each mark stands for a fixed number of coppers: `I` is 1, `V` is 5, `X` is 10, `L` is 50, `C` is 100, `D` is 500, and `M` is 1000.

A price is a string `tag` made of these marks, read left to right.
When a mark's value is smaller than the value of the mark immediately after it, the smaller value is subtracted from the total.
Otherwise the mark's value is added.
For example, `XIV` is the price 14: `X` adds 10, `I` comes before the larger `V` and is subtracted, and `V` adds 5.
Tags never contain more than four copies of the same mark.

Return the price in coppers for the given `tag`.

Let `n` be the number of marks in `tag`; `1 <= n <= 15`.
"""
import unittest
import itertools

NUMERALS = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

def tallyPrice(tag):
    """Return the price in coppers for the tag."""
    groups = [(NUMERALS[i], len(list(j))) for i, j in itertools.groupby(tag)]
    total = 0
    while groups:
        amount, count = groups.pop(0)
        sign = 1
        if groups and amount < groups[0][0]:
            sign = -1
        total += sign * amount * count
    return total


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(tallyPrice("VII"), 7)
        self.assertEqual(tallyPrice("LXXXVII"), 87)
        self.assertEqual(tallyPrice("MMMDCCCLXXXVIII"), 3888)

if __name__ == "__main__":
    unittest.main()
