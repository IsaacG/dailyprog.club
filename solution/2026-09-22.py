"""The Confectioner's Window

A confectioner arranges a row of identical sweets in the shop window, one sweet per slot.
The sweets come in a few flavours; sweets of the same flavour are indistinguishable, so two rows that differ only by swapping two same-flavoured sweets are the same display.

Given the string `letters`, where each character names the flavour of one sweet and the string length is the number of sweets, return how many distinct rows can be made using every sweet.

### Constraints

* 1 <= the length of `letters` <= 12
* `letters` contains only lowercase letters
* every answer fits in a 32-bit integer
"""
import unittest

import collections
import math

def countOrderings(letters):
    """Return the number of distinct orderings of the letters."""
    ways = 1
    n = len(letters)
    for count in collections.Counter(letters).values():
        ways *= math.comb(n, count)
        n -= count
    return ways


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(countOrderings("abcdef"), 720)
        self.assertEqual(countOrderings("aab"), 3)
        self.assertEqual(countOrderings("aaaa"), 1)
        self.assertEqual(countOrderings("aabbcc"), 90)
        self.assertEqual(countOrderings("abacaba"), 105)
        self.assertEqual(countOrderings("aaaaabbbbbcc"), 16632)

if __name__ == "__main__":
    unittest.main()
