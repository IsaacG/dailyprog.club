"""Chalk Lines on the Parade Street

Before the harvest parade, each float crew chalks off a stretch of the long main street to build on, measured in whole paces along it.
Each claim is a pair [start, end] in `spans`, where span i claims every pace from `spans[i][0]` up to but not including `spans[i][1]`.
A claim counts as standing on its own ground when at least one pace it covers is covered by no other claim.
Return the sorted list of the zero-based positions of the claims that stand on their own ground, or an empty list if none do.

### Constraints

* 1 <= number of claims <= 30
* every start and end is an integer from 0 to 1000000000 inclusive
"""
import unittest

def aloneItems(spans):
    """Return the sorted positions of the spans that have at least one cell to themselves."""
    starts = sorted(enumerate(i[0] for i in spans), key=lambda x: x[1], reverse=True)
    ends = sorted(enumerate(i[1] for i in spans), key=lambda x: x[1], reverse=True)
    points = sorted({j for i in spans for j in i})

    active = set()
    out = set()
    for pos in points:
        while ends and ends[-1][1] == pos:
            active.remove(ends.pop()[0])
        while starts and starts[-1][1] == pos:
            active.add(starts.pop()[0])
        if len(active) == 1:
            out.add(list(active)[0])
    return sorted(out)

class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(aloneItems([[0, 10], [3, 6]]), [0])
        self.assertEqual(aloneItems([[0, 5], [0, 2]]), [0])
        self.assertEqual(aloneItems([[0, 2], [2, 4]]), [0, 1])
        self.assertEqual(aloneItems([[0, 5], [0, 5], [0, 5]]), [])
        self.assertEqual(aloneItems([[0, 2], [2, 4], [0, 4]]), [])
        self.assertEqual(aloneItems([[5, 10], [0, 7]]), [0, 1])
        self.assertEqual(aloneItems([[7, 9]]), [0])
        self.assertEqual(aloneItems([[0, 1000000000], [500000000, 1000000000]]), [0])
        self.assertEqual(aloneItems([[0, 50], [0, 10], [100, 150], [100, 110], [200, 250], [200, 210], [300, 350], [300, 310], [400, 450], [400, 410], [500, 550], [500, 510], [600, 650], [600, 610], [700, 750], [700, 710], [800, 850], [800, 810], [900, 950], [900, 910], [2000, 2004], [2010, 2014], [2020, 2024], [2030, 2034], [2040, 2044], [2050, 2054], [2060, 2064], [2070, 2074], [2080, 2084], [2090, 2094]]), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29])

if __name__ == "__main__":
    unittest.main()
