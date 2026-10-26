"""Restringing the Harp Row

The harp row has to be restrung before the evening concert, and the crew can trade the positions of any two harps in the row.

You are given the row as it stands this morning in `start`, where `start[i]` is the harp occupying place i, and the arrangement the stage plan calls for in `target`, where `target[i]` is the harp that belongs in place i.
Both hold the same harps, each appearing once.
Given also `limit`, the number of trades the crew has time for, return `true` if the row can reach the stage plan using at most `limit` trades, and `false` otherwise.
Using fewer trades than allowed is fine.

### Constraints

* 1 <= n <= 50, where `n` is the number of harps in each row
* every value in `start` and `target` is a non-negative integer
* the two rows hold the same harps, each exactly once
* 0 <= limit
"""
import unittest

def canRestring[T](start: list[T], target: list[T], limit: int) -> bool:
    """Return True if the target arrangement is reachable within the swap limit."""
    todo = {i for i, (a, b) in enumerate(zip(start, target)) if a != b}
    idx_by_val = {val: idx for idx, val in enumerate(start) if idx in todo}
    swaps = 0
    while todo and swaps < limit:
        target_idx = todo.pop()
        src_idx = idx_by_val.pop(target[target_idx])
        start[target_idx], start[src_idx] = start[src_idx], start[target_idx]
        if start[src_idx] == target[src_idx]:
            todo.remove(src_idx)
        idx_by_val[start[src_idx]] = src_idx
        swaps += 1
    return not todo


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(canRestring([4, 7, 2, 9], [7, 4, 2, 9], 1), True)
        self.assertEqual(canRestring([1, 2, 0, 3], [0, 1, 2, 3], 1), False)
        self.assertEqual(canRestring([1, 2, 3, 0], [0, 1, 2, 3], 2), False)
        self.assertEqual(canRestring([4, 7, 2, 9], [7, 4, 2, 9], 2), True)
        self.assertEqual(canRestring([9, 5, 1, 3], [1, 5, 9, 3], 1), True)
        self.assertEqual(canRestring([1, 0, 2], [0, 1, 2], 0), False)
        self.assertEqual(canRestring([8, 3], [3, 8], 1), True)
        self.assertEqual(canRestring([5], [5], 0), True)
        self.assertEqual(canRestring([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], 0), True)

if __name__ == "__main__":
    unittest.main()
