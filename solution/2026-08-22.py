"""The Pruning of Starlight

Last night the whispering seeds were sorted into their clay pots; tonight the Moon Garden answers another sign.
Starlight vines have knitted themselves into one long garland around the trellis, and each segment carries a number cut into its skin.
Elder Thorne reads the tangle and says the century-flower will not open unless the garland is pruned to spell the smallest constellation it can.
So the Work goes tonight: burned down to nothing but essence.

Brother Moss must cut away exactly k segments.
The segments that remain keep their original left-to-right order, and the list of numbers they carry must be as small as possible when compared from left to right: at the first position where two candidates differ, the smaller number makes that candidate smaller.
He may cut any k segments, not necessarily adjacent ones.

Given the array `marks` (where `marks[i]` is the number carved on segment i) and the integer `k`, return the remaining list of integers.
If every segment is cut, return an empty array.

### Constraints

* 1 <= n <= 40, where n is the length of `marks`
* 0 <= k <= n
* -100 <= marks[i] <= 100
"""
import unittest

def pruneVines(marks, k):
    """Return the smallest remaining sequence."""
    if k >= len(marks):
        return []
    if k == 0:
        return marks
    pick = marks.index(min(marks[:k + 1]))
    return marks[pick:pick + 1] + pruneVines(marks[pick + 1:], k - pick)


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(pruneVines([3, 1, 4, 2], 2), [1, 2])
        self.assertEqual(pruneVines([5, 4, 3, 2, 1], 2), [3, 2, 1])
        self.assertEqual(pruneVines([1, 2, 3], 0), [1, 2, 3])

if __name__ == "__main__":
    unittest.main()
