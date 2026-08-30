"""The Century-Flower Opens

On the seventh night the moon slides into the earth's shadow and turns copper, and the hundred-year bud at the garden's heart begins to tremble.
Elder Thorne, Sister Lune, and Brother Moss join hands in a circle around it.
All the Work of the waxing has led here: night after night, rite after rite, the Gardeners have lashed root to root beneath the soil, and Elder Thorne has kept every binding in his ledger, in the order the rites were performed.
The century-flower will not open for light that only part of the garden tastes.
It unfurls at the exact moment the eclipse light drawn in by any one root can pass, binding by binding, to every root in the garden: the moment the garden first drinks as one.

There are `n` roots, numbered 0 through n-1, and before the first binding each root drinks alone.
The ledger's two columns are the equal-length lists `left` and `right`: line i of the ledger records the binding of root `left[i]` to root `right[i]`.
A binding lets the drink pass both ways between its two roots, and what a root drinks it shares onward through every binding it has, so two roots drink together whenever any chain of bindings joins them.

Read the ledger in order, oldest line first.
Return the position in the ledger, counted from 1, of the line at which all `n` roots first drink together, or -1 if the ledger runs out with the garden still parted.
A line that binds two roots already drinking together changes nothing beneath the soil, and a line may even name the same root twice; the rite was performed all the same, and the line keeps its place in the ledger's count.

Constraints: 2 <= `n` <= 500. `left` and `right` have the same length `m`, the number of lines in the ledger, with 0 <= `m` <= 500, and every entry in both is a root number from 0 to n-1.
"""
import unittest

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


def bloomBinding(n, left, right):
    "Return the 1-based ledger position where all roots first drink together, or -1."""
    if len(left) < n - 1:
        return -1
    unbound = set(range(n))
    sets = [{i} for i in range(n)]
    for i, (a, b) in enumerate(zip(left, right), 1):
        if len(add_to_disjoint_sets(sets, {a, b})) == n:
            return i
    return -1


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(bloomBinding(5, [0, 1, 0, 2, 3], [1, 2, 2, 3, 4]), 5)
        self.assertEqual(bloomBinding(4, [0, 1, 0], [1, 2, 2]), -1)
        self.assertEqual(bloomBinding(2, [0, 1], [1, 0]), 1)

if __name__ == "__main__":
    unittest.main()
