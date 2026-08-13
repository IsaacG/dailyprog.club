"""The compositor's tray

Old Hesper ran the print shop on Candle Row for forty years and never once wrote his method down.
When they cleared the loft they found only this: a bundle of manuscripts, each still pinned to the sheet his press had produced from it.

The shop reopens next month.
Work out what the press did, then do it: given a `manuscript` of lowercase letters, return the sheet.

**The rule is written down nowhere but the examples.** They were chosen to pin it down completely: every behaviour the hidden tests exercise is already demonstrated below.
Nothing new is waiting for you.

The manuscript is lowercase `a`–`z` only, may be empty, and is at most 400 letters long.
"""
import unittest
import collections
import string


def setType(manuscript):
    "Return the sheet Hesper's press would produce."
    shift = collections.defaultdict(int)
    out = ""
    for i in manuscript:
        out += string.ascii_lowercase[(string.ascii_lowercase.index(i) + shift[i]) % 26]
        shift[i] += 1
    return out


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(setType("abc"), "abc")
        self.assertEqual(setType("aaa"), "abc")
        self.assertEqual(setType("aab"), "abb")
        self.assertEqual(setType("banana"), "banboc")
        self.assertEqual(setType("zz"), "za")

if __name__ == "__main__":
    unittest.main()
