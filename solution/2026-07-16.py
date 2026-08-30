"""Talk Scheduling

You are organizing a conference with `n` talks, numbered from 0 to n-1.
You have a list of dependencies: each dependency `[a, b]` means talk `a` must be scheduled before talk `b`.
Determine if it's possible to schedule all talks respecting all dependencies (i.e., no circular prerequisites).
Return `true` if possible, otherwise `false`.
"""
import unittest
import collections

def canFinishAll(n, dependencies):
    """Return True if all talks can be scheduled without cycle, else False."""
    deps = collections.defaultdict(set)
    for a, b in dependencies:
        deps[b].add(a)
    can_do = {i for i in range(n) if i not in deps}
    todo = set(range(n)) - can_do
    while todo:
        add = next((i for i in todo if deps[i] <= can_do), None)
        if add is None:
            return False
        todo.remove(add)
        can_do.add(add)
    return True


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(canFinishAll(2, [[0, 1]]), True)
        self.assertEqual(canFinishAll(3, []), True)
        self.assertEqual(canFinishAll(2, [[0, 1], [1, 0]]), False)
        self.assertEqual(canFinishAll(1, [[0, 0]]), False)
        self.assertEqual(canFinishAll(12, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 0]]), False)
        self.assertEqual(canFinishAll(0, []), True)
        self.assertEqual(canFinishAll(4, [[0, 1], [2, 3]]), True)

if __name__ == "__main__":
    unittest.main()
