"""In Equal Measure

The Maker divided the light from the darkness, and evening and morning were the first day.

The first hours are set down in `sky`, a string in which `sky[i]` is `L` if hour i was light and `D` if it was dark.
Somewhere in that record lies the longest unbroken stretch of hours in which light and darkness were held in equal measure: as many hours of light as hours of darkness.
Return the number of hours in that stretch, or 0 if no stretch of the record qualifies.

Constraints: `0 <= n <= 1000`, where `n` is the number of hours in `sky`, and every character of `sky` is `L` or `D`.
"""
import unittest
import itertools

def equalMeasure(sky):
    """Return the length of the longest stretch with as many light hours as dark hours."""
    return min(sky.count("D"), sky.count("L")) * 2
    first_seen = {0: -1}
    best = delta = 0
    for idx, i in enumerate(sky):
        delta += 1 if i == "D" else -1
        best = max(best, idx - first_seen.get(delta, idx))
        first_seen.setdefault(delta, idx)
    return best


    runs = [0, 0] + [len(list(i)) for _, i in itertools.groupby(sky)] + [0]
    return 2 * max(
        b if b <= a + c else 0
        for a, b, c in zip(runs[0:], runs[1:], runs[2:])
    )



class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(equalMeasure("DDLLLDLL"), 6)
        self.assertEqual(equalMeasure("LLLDDD"), 6)
        self.assertEqual(equalMeasure("LLLL"), 0)
        self.assertEqual(equalMeasure(""), 0)
        self.assertEqual(equalMeasure("DLDLDL"), 6)
        self.assertEqual(equalMeasure("DLLDLDL"), 6)
        self.assertEqual(equalMeasure("DLDDLDL"), 6)
        self.assertEqual(equalMeasure("DDLLLLLDLL"), 4)
        self.assertEqual(equalMeasure("DDLLDLL"), 6)
        self.assertEqual(equalMeasure("DDLLDDDLLL"), 10)
        self.assertEqual(equalMeasure("DDDLLLDDLL"), 10)
        self.assertEqual(equalMeasure("DLLLDDDL"), 8)
        self.assertEqual(equalMeasure("LDLDLD"), 6)

if __name__ == "__main__":
    unittest.main()
