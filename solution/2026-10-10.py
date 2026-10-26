"""Critical Path in the Rigging Loft

A shipyard schedules hull sections through the rigging loft.
Each section `i` needs `durations[i]` hours of crane time, and a section can only begin once every section listed as its prerequisite has finished.
Any number of sections may be worked at once.

`deps` is a list of ordered pairs `[a, b]`: section `a` must finish before section `b` may start.
No pair points a section at itself, no pair repeats, and the pairs never form a loop.

A section is *pressing* if delaying its own start by one hour, while every other section still starts as early as it can, would push the whole yard's finish later.

Return the numbers of all pressing sections, in increasing order.

### Constraints

* 2 <= n <= 12, where `n` is the number of sections
* each `durations[i]` is an integer from 1 to 1000 inclusive
* 1 <= the number of pairs in `deps` <= 10
"""
import unittest
import collections

def pressingSections(durations, deps):
    """Return the indices of the critical tasks, in increasing order."""
    # Add an extra node that depends on all the prior nodes.
    durations.append(0)
    # Collect the prereqs for each node.
    reqs = collections.defaultdict(set)
    for a, b in deps:
        reqs[b].add(a)
    todo = set(range(len(durations)))
    # Set the prereqs for the last node to be all other leaf nodes.
    reqs[len(durations) - 1] = todo - {a for a, _ in deps} - {len(durations) - 1}
    earliest = {}
    # Compute the earliest start for each segment.
    while todo:
        can_do = next(i for i in todo if set(earliest) >= reqs[i])
        todo.remove(can_do)
        earliest[can_do] = max((earliest[i] + durations[i] for i in reqs[can_do]), default=0)

    # Walk the critical path from the extra node to the root.
    critical = set()
    crits = {len(durations) - 1}
    while crits:
        crits = {i for c in crits for i in reqs[c] if earliest[i] + durations[i] == earliest[c]}
        critical.update(crits)
    return sorted(critical)


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(pressingSections([3, 2, 4, 3], [[0, 1], [1, 2], [0, 3]]), [0, 1, 2])
        self.assertEqual(pressingSections([2, 2, 3, 3], [[0, 2], [1, 3]]), [0, 1, 2, 3])
        self.assertEqual(pressingSections([1, 5, 20], [[0, 1]]), [2])
        self.assertEqual(pressingSections([1, 1, 1, 1, 3], [[0, 1], [1, 2], [2, 3], [4, 3]]), [0, 1, 2, 3, 4])
        self.assertEqual(pressingSections([1, 1, 10], [[2, 0], [2, 1]]), [0, 1, 2])
        self.assertEqual(pressingSections([5, 5, 5], [[0, 1], [1, 2]]), [0, 1, 2])
        self.assertEqual(pressingSections([4, 2, 3, 6, 5, 2, 3, 2, 1, 1, 2, 2], [[0, 5], [3, 5], [1, 4], [2, 4], [4, 6], [5, 6], [6, 7], [7, 8], [9, 10], [10, 11]]), [2, 3, 4, 5, 6, 7, 8])

if __name__ == "__main__":
    unittest.main()
