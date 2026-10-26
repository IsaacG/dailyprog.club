"""Seating the Banquet Rounds

A banquet steward is laying out place cards for a long head table.
The cards arrive as a string of lowercase letters, one letter per guest's family name, in no particular order.
The steward may shuffle the cards into any arrangement at all, but two guests from the same family must never end up seated side by side.

Given `letters`, return true if some ordering of the cards keeps every pair of equal letters apart, and false otherwise.

### Constraints

* The string `letters` has at least 1 and at most 20 characters.
* Every character in `letters` is a lowercase English letter.
"""
import unittest
import collections

def canArrangeApart(letters):
    """Return True if the characters can be reordered so that no two equal characters are adjacent."""
    return collections.Counter(letters).most_common(1)[0][1] - 1 < (len(letters) + 1) // 2


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(canArrangeApart("aabb"), True)
        self.assertEqual(canArrangeApart("aa"), False)
        self.assertEqual(canArrangeApart("aab"), True)
        self.assertEqual(canArrangeApart("z"), True)
        self.assertEqual(canArrangeApart("aaab"), False)
        self.assertEqual(canArrangeApart("aaabbb"), True)
        self.assertEqual(canArrangeApart("aaaaaaaaaaabbbbbbbbb"), False)

if __name__ == "__main__":
    unittest.main()
