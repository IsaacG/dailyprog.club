"""The Archivist's Ledger

In a great library, every subject is stored in a single drawer.
Each drawer has a call number, and it may split into a left sub-drawer and a right sub-drawer.
The archivist's law: every call number found anywhere in a drawer's left branch must be strictly smaller than the drawer's own number, and every call number found anywhere in its right branch must be strictly larger.

You are given three arrays, each of length `n`:

* `numbers[i]` is the call number on drawer `i`.
* `left[i]` is the index of drawer `i`'s left sub-drawer, or `-1` if there is none.
* `right[i]` is the index of drawer `i`'s right sub-drawer, or `-1` if there is none.

Drawer `0` is the main drawer.
Every drawer is reachable from it, and no drawer has two parents.

Return `true` if the archive obeys the archivist's law, and `false` otherwise.

Constraints: `0 <= n <= 50`; each call number is an integer between `-10^9` and `10^9`; each child index is `-1` or a valid drawer index.
"""
import unittest

def validCatalog(numbers, left, right):
    """Return if the archive obeys the archivist's law."""

    def check(idx, lo, hi):
        number = numbers[idx]
        if lo is not None and lo >= number or hi is not None and hi <= number:
            return False
        if (l := left[idx]) != -1 and not check(l, lo, number):
            return False
        if (r := right[idx]) != -1 and not check(r, number, hi):
            return False
        return True

    return not numbers or check(0, None, None)


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(validCatalog([8, 3, 10], [1, -1, -1], [2, -1, -1]), True)
        self.assertEqual(validCatalog([5, 1, 4], [1, -1, -1], [2, -1, -1]), False)
        self.assertEqual(validCatalog([42], [-1], [-1]), True)
        self.assertEqual(validCatalog([], [], []), True)

if __name__ == "__main__":
    unittest.main()
