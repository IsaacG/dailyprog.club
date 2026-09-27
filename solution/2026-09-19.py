"""As Each Came to Be Named

The Maker said, let the earth bring forth living creatures according to their kinds, cattle and creeping things and beasts of the earth; then made the Man and the Woman, blessed them, and gave them the Garden to keep; and there was evening and there was morning, the sixth day, and it was very good.

The creatures came before the Man in single file, and he named them in the order they arrived, front to back.
The order itself was not written down; only a record of each creature was. `creatures[i]` is a pair `[height, blocked]`: the creature's height in cubits, and how many of the creatures ahead of it in the line were at least as tall as it.
The record is in no particular order, and exactly one line fits it.
Return the heights in line order, from the first creature named to the last.

For example, the record `[[7, 0], [5, 2], [5, 0]]` fits only the line 5, 7, 5: the last 5 has two creatures at least as tall ahead of it, the 7 and the other 5.

Constraints: `1 <= n <= 50`, where `n` is the number of creatures in `creatures`; each `height` is an integer from 1 to 100, and each `blocked` is an integer from 0 to n-1.
"""
import unittest
import itertools

def namingOrder(creatures):
    """Return the heights in the order the Man named the creatures."""
    out = []
    for want_blocked, group in itertools.groupby(sorted(creatures, key=lambda x: (x[1], x[0])), key=lambda x: x[1]):
        idx = 0
        for height, _ in group:
            has_blocked = sum(i >= height for i in out[:idx])
            while has_blocked < want_blocked:
                if out[idx] >= height:
                    has_blocked += 1
                idx += 1
            out.insert(idx, height)
            idx += 1
    return out


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(namingOrder([[5, 0], [4, 1], [6, 0], [6, 1], [4, 4], [7, 0]]), [5, 4, 6, 6, 4, 7])
        self.assertEqual(namingOrder([[6, 1], [6, 3], [6, 2], [6, 0]]), [6, 6, 6, 6])
        self.assertEqual(namingOrder([[5, 4], [6, 3], [8, 1], [7, 2], [9, 0]]), [9, 8, 7, 6, 5])
        self.assertEqual(namingOrder([[9, 0]]), [9])
        self.assertEqual(namingOrder([[3, 0], [4, 0], [5, 0], [3, 1], [5, 1]]), [3, 3, 4, 5, 5])
        self.assertEqual(namingOrder([[3, 0], [5, 0], [7, 0], [4, 1], [7, 1]]), [3, 5, 4, 7, 7])
        self.assertEqual(namingOrder([[3, 0], [4, 0], [5, 0], [4, 1], [4, 2], [3, 4]]), [3, 4, 4, 4, 3, 5])
        self.assertEqual(namingOrder([[3, 0], [4, 0], [5, 0], [3, 1], [4, 1]]), [3, 3, 4, 4, 5])
        self.assertEqual(namingOrder([[3, 0], [4, 0], [5, 0], [3, 1], [4, 2]]), [3, 3, 4, 5, 4])

if __name__ == "__main__":
    unittest.main()
