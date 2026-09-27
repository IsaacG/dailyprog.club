"""The Paper Trail

At an office, `n` forms sit in an in-tray, numbered `0` through `n - 1`.
The tray also holds `m` routing slips.
Slip `i` names two forms: form `before[i]` must be stamped before form `after[i]`.

Return `1` if a clerk can stamp every form in one order that honors every routing slip, or `0` if the slips make such an order impossible.
A form that appears on no slip can be stamped any time.

Constraints: `0 <= n <= 12`, `0 <= m <= 12`, and every value in `before` and `after` is an integer from `0` to `n - 1`.
"""
import unittest
import collections

def canSignAll(n, before, after):
    # return 1 if every form can be stamped in a slip-respecting order, else 0
    prereqs = collections.defaultdict(set)
    for b, a in zip(before, after):
        prereqs[a].add(b)
    todo = {i for i in range(n) if i in prereqs}
    while todo:
        can_do = next(
            (
                i
                for i in todo
                if all(prereq not in todo for prereq in prereqs[i])
            ), None
        )
        if can_do is None:
            return 0
        todo.remove(can_do)
    return 1

class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(canSignAll(4, [0, 1, 2], [1, 2, 3]), 1)
        self.assertEqual(canSignAll(2, [0, 1], [1, 0]), 0)
        self.assertEqual(canSignAll(4, [], []), 1)

if __name__ == "__main__":
    unittest.main()
