"""The Hive's Sealed Chambers

A beekeeper maps a hive frame as a grid of cells, each either open comb or waxed shut.
Open cells that share an edge form one chamber.
A chamber is sealed if none of its cells touches the frame's outer edge.
Given `cells` in row-major order and the frame's `width`, return the sizes of all sealed chambers, largest first, or an empty array if none are sealed.

`cells[i]` is 0 for an open cell and 1 for a waxed cell.
Two open cells share an edge when one is directly above, below, left, or right of the other.
The outer edge is the first and last row and the first and last column.

### Constraints

* 1 <= number of cells <= 48
* each cell value is 0 or 1
* 1 <= width <= 48
* the number of cells is a whole number of rows of `width`
"""
import unittest

import itertools

# 2026-08-27 2026-07-18 2026-10-01
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

def pocketSizes(cells, width):
    """Return the sizes of the sealed regions, largest first."""
    height = len(cells) // width
    # Collect the (x, y) for all open cells.
    cells = {(x, y) for y, row in enumerate(itertools.batched(cells, n=width)) for x, cell in enumerate(row) if cell == 0}
    # Start off with each cell as its own group of one cell.
    groups = [{i,} for i in cells]
    # Merge each open cell with its neighbor to the right or down.
    for x, y in cells:
        if (x + 1, y) in cells:
            add_to_disjoint_sets(groups, {(x, y), (x + 1, y)})
        if (x, y + 1) in cells:
            add_to_disjoint_sets(groups, {(x, y), (x, y + 1)})
    # Find edge cells. Remove groups that include an edge.
    edges = {(x, y) for (x, y) in cells if x == 0 or y == 0 or x == width - 1 or y == height - 1}
    groups = [group for group in groups if all(i not in edges for i in group)]
    # Return sorted sizes.
    return sorted((len(i) for i in groups), reverse=True)


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(pocketSizes([1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1], 7), [1, 1, 1])
        self.assertEqual(pocketSizes([1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1], 5), [4])
        self.assertEqual(pocketSizes([1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1], 5), [5])
        self.assertEqual(pocketSizes([1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 5), [1, 1])
        self.assertEqual(pocketSizes([1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1], 5), [])
        self.assertEqual(pocketSizes([1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1], 6), [4, 1])
        self.assertEqual(pocketSizes([0], 1), [])
        self.assertEqual(pocketSizes([1, 1, 0, 1, 1, 1], 6), [])
        self.assertEqual(pocketSizes([1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 8), [4, 4, 2])

if __name__ == "__main__":
    unittest.main()
