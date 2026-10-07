"""The Harbor Rigger's Manifest

A harbor rigger logs mooring lines, and each line in the log says two buoy tags belong to the same mooring.
The log is `links`, a flat list of even length where `links[2i]` and `links[2i+1]` name the same mooring.
Every value in the list names a buoy tag, and two tags share a mooring if a line names them together or if a chain of lines connects them.
Return the sizes of the distinct moorings, from smallest to largest.
An empty log gives an empty array.

### Constraints

* the log has between 0 and 40 entries, and its length is always even
* every buoy tag is an integer from 0 to 99 inclusive
"""
import unittest
import itertools

# 2026-08-27.py
# 2026-07-18.py
# Taken from my AoC helper lib.
def add_to_disjoint_sets[T](sets: list[set[T]], new: set[T]) -> set[T]:
    """Add in-place a new set to a list of disjoint sets. Return the newly added combined set."""
    for a in list(sets):
        if a & new:
            sets.remove(a)
            a |= new
            return add_to_disjoint_sets(sets, a)
    sets.append(new)
    return new


def mooringSizes(links):
    # TODO: return the sizes of the distinct items, smallest first
    sets = []
    for a, b in itertools.batched(links, 2):
        add_to_disjoint_sets(sets, {a, b})
    return sorted(len(i) for i in sets)


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(mooringSizes([0, 1, 2, 1]), [3])
        self.assertEqual(mooringSizes([0, 1, 2, 3]), [2, 2])
        self.assertEqual(mooringSizes([0, 1, 2, 3, 1, 2]), [4])
        self.assertEqual(mooringSizes([0, 1, 1, 2, 3, 4]), [2, 3])
        self.assertEqual(mooringSizes([]), [])

if __name__ == "__main__":
    unittest.main()
