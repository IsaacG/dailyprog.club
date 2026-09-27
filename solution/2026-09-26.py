"""Rearranging the Locker Roster

The staff lockers at the observatory are numbered from 0 upward, and each locker holds a numbered key tag. `order` is a list where `order[i]` is the tag currently sitting in locker i.
A swap exchanges the tags in two lockers of your choosing.

`mustFix` is a list of distinct locker positions.
Return the fewest swaps needed so that each locker in `mustFix` ends up holding the tag whose number equals that locker's number.
Lockers not in `mustFix` may end up holding any tag at all.
If `mustFix` is empty, the answer is 0.

### Constraints

* `order` has n entries, where 1 <= n <= 1000, and holds each number from 0 to n - 1 exactly once.
* `mustFix` has between 0 and n entries, each a distinct locker position from 0 to n - 1.
"""
import unittest

def countSwaps(order, mustFix):
    """Return the fewest swaps needed to fix every listed index."""
    val_by_idx = {idx: val for idx, val in enumerate(order) if idx in mustFix or val in mustFix}
    idx_by_val = {val: idx for idx, val in enumerate(order) if idx in mustFix or val in mustFix}
    swaps = 0
    while mustFix:
        target_val = target_idx = mustFix.pop()
        src_idx = idx_by_val.pop(target_val)
        src_val = val_by_idx.pop(target_idx)
        if src_idx == target_idx:
            continue
        val_by_idx[src_idx] = src_val
        idx_by_val[src_val] = src_idx
        swaps += 1
    return swaps


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(countSwaps([1, 0, 2], [0, 1]), 1)
        self.assertEqual(countSwaps([1, 0, 2], []), 0)
        self.assertEqual(countSwaps([1, 2, 3, 4, 0], [0]), 1)
        self.assertEqual(countSwaps([0, 1, 2], [0, 1, 2]), 0)
        self.assertEqual(countSwaps([0, 2, 1], [0]), 0)
        self.assertEqual(countSwaps([1, 2, 0], [0, 1, 2]), 2)
        self.assertEqual(countSwaps([2, 1, 0, 3], [1]), 0)
        self.assertEqual(countSwaps([1, 0, 3, 2], [0, 2]), 2)
        self.assertEqual(countSwaps([1, 2, 3, 0, 4], [0, 2]), 2)

if __name__ == "__main__":
    unittest.main()
