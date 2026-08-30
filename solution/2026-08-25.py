"""A Ladder of Light

On the fifth night the moon rises fat and golden over the Moon Garden.
Elder Thorne trims the spent heads of the old lunar lilies, and their silver pollen drifts down onto the waiting plot, sprinkling the soil with faintly glowing specks.
Sister Lune walks the rows before the dew can dull them and records each speck's glow, a whole number of glimmers, in the list `glows`: `glows[i]` is the glow of the i-th speck she reads.

Brother Moss says the century-flower will not climb toward bloom on scattered light; it needs a ladder.
A ladder is a set of glow values that follow one another one glimmer apart with no rung missing, like glows of 6, 7, 8, and 9.
Where a speck lies in the plot does not matter, and the rungs of a ladder may be read in any order.
Two specks that share a glow light the same rung: one speck is enough, and a second adds nothing.
Return the number of rungs in the longest ladder the fallen pollen lights.
A single speck always lights a ladder of one rung.

Constraints: 1 <= n <= 500, where `n` is the number of specks in `glows`.
Each glow is an integer from 0 to 100000.
"""
import unittest

def longestLadder(glows):
    """Return the number of rungs in the longest ladder the pollen lights."""
    run, longest = 1, 1
    glows = sorted(set(glows))
    for a, b in zip(glows, glows[1:]):
        if a + 1 == b:
            run += 1
            longest = max(longest, run)
        elif a < b:
            run = 1
    return longest

class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(longestLadder([7, 2, 9, 4, 3, 8, 1, 21, 8]), 4)
        self.assertEqual(longestLadder([12]), 1)
        self.assertEqual(longestLadder([5, 5, 5, 5]), 1)

if __name__ == "__main__":
    unittest.main()
