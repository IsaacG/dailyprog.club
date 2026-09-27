"""The First Rain

The Maker set an expanse amid the waters, dividing the waters above from the waters below, and named the expanse Sky.
Then the first rain let go of the waters above.

Every drop let go at the same moment, but from its own height and at its own pace. `heights` lists the drops from the lowest to the highest: drop i let go `heights[i]` cubits above the Deep, and no two drops let go from the same height. `paces` lists the same drops in the same order: drop i falls `paces[i]` cubits in an hour.
A drop cannot pass through a drop beneath it: when it catches up with one, the two join and fall on together at the pace of the lower drop, and a drop that has taken in others can be caught in the same way.
Drops that would reach the Deep at the same moment reach it as one.
Each drop that strikes the Deep is made of one or more of the drops that let go; return those counts, in the order the drops strike the Deep.

Constraints: `1 <= n <= 1000`, where `n` is the number of drops in `heights` and in `paces`; each height is an integer from 1 to 10000, and the heights strictly increase; each pace is an integer from 1 to 100.
"""
import unittest


def firstRain(heights, paces):
    """Return how many drops each drop that strikes the Deep is made of, in the order they strike it."""
    out = []
    todo = [h / p for h, p in zip(heights, paces)]
    todo.reverse()
    while todo:
        count = 1
        impact = todo.pop()
        while todo and todo[-1] <= impact:
            todo.pop()
            count += 1
        out.append(count)
    return out


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(firstRain([2, 5, 7, 12], [1, 5, 1, 4]), [2, 2])
        self.assertEqual(firstRain([3, 6, 8], [3, 3, 8]), [1, 2])
        self.assertEqual(firstRain([1, 2, 3], [1, 1, 1]), [1, 1, 1])

if __name__ == "__main__":
    unittest.main()
