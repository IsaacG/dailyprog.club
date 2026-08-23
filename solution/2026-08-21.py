"""The Fullest Pot

On the first night of the moon's last waxing, the Night Gardeners begin the Work that will open the century-flower, which blooms once in a hundred years.
Elder Thorne pours a mound of pale whispering seeds onto the stone table, and Sister Lune must bed every one of them in clay pots before dawn, each seed settling into its bed as its faint voice goes quiet.

Each seed whispers for one stretch of the night, and two arrays of equal length describe the mound: `starts` holds the moment each whisper begins and `ends` the moment it fades, so seed i whispers from moment `starts[i]` through moment `ends[i]` and is still whispering at both of those moments.
Seeds whose whispers share even a single moment are kin, and kin must be bedded together in one pot.
When one seed falls silent at the very moment another wakes, that shared moment makes them kin as well.
Kinship also carries: a seed is bedded with all the kin of its kin, even those it never whispered beside.

Sister Lune fills one pot for each fellowship of kin, and a seed with no kin sleeps alone in its own pot.
Return the number of seeds in the fullest pot.

Constraints: `1 <= n <= 500`, where `n` is the length of both `starts` and `ends`.
Each `starts[i]` and `ends[i]` is an integer with `0 <= starts[i] <= ends[i] <= 10^9`.
"""
import unittest
import collections

def fullestPot(starts, ends):
    """Return the number of seeds in the fullest pot."""
    starts = collections.deque(sorted(starts))
    ends = collections.deque(sorted(ends))

    most = 0
    cur = 0
    ongoing = 0
    while starts:
        while starts and starts[0] <= ends[0]:
            starts.popleft()
            cur += 1
            ongoing += 1
            most = max(most, cur)
        while starts and ends[0] < starts[0]:
            ends.popleft()
            ongoing -= 1
            if not ongoing:
                cur = 0
    return most


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(fullestPot([6, 1, 4, 9], [8, 5, 7, 12]), 3)
        self.assertEqual(fullestPot([1, 3], [3, 6]), 2)
        self.assertEqual(fullestPot([0, 4, 8], [2, 6, 10]), 1)

if __name__ == "__main__":
    unittest.main()
