"""The Lost Connection

A colony of starships communicates through warp gates.
Each gate connects two ships.
However, too many connections can create a warp resonance, that is, a cycle of gates that links back to the starting ship.
The engineers are adding gates one by one.
Find the index of the first gate that, when added, creates a cycle.
If no cycle is ever created, return -1.
"""
import unittest

# From AoC pylib
def add_to_disjoint_sets(sets: list[set[T]], new: set[T]) -> set[T]:
    """Add in-place a new set to a list of disjoint sets. Return the newly added combined set."""
    for a in list(sets):
        if a & new:
            sets.remove(a)
            a |= new
            return add_to_disjoint_sets(sets, a)
    sets.append(new)
    return new

def firstWarpCycle(gates):
    """Return the 0-based index of the first gate that creates a cycle, or -1.

    Maintain a set of linked (non-cyclic) ships.
    Check if any given pair is in an existing set.
    If the pair is already in the set, this introduces a cycle.
    """
    linked = []
    for i, pair in enumerate(set(i) for i in gates):
        if any(pair.issubset(group) for group in linked):
            return i
        add_to_disjoint_sets(linked, pair)
    return -1



class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(firstWarpCycle([[0, 1], [1, 2], [2, 0], [3, 4]]), 2)
        self.assertEqual(firstWarpCycle([[0, 1], [2, 3], [4, 5]]), -1)
        self.assertEqual(firstWarpCycle([[0, 1]]), -1)
        self.assertEqual(firstWarpCycle([[0, 1], [2, 3], [1, 2], [0, 3]]), 3)
        self.assertEqual(firstWarpCycle([[0, 1], [1, 2], [2, 3], [3, 4], [0, 4]]), 4)
        self.assertEqual(firstWarpCycle([]), -1)

if __name__ == "__main__":
    unittest.main()
