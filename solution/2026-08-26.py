"""The Silent Rounds

On the night before the eclipse, the Moon Garden falls silent.
Elder Thorne, Sister Lune, and Brother Moss walk the moonflower path, their footsteps the only sound.
The century-flower waits, and dew has gathered unevenly on the leaves.
With each faint breath of wind, any leaf that holds more dew than the leaf to its right lets one drop roll to the right.
You are asked to record the garden round by round.
Elder Thorne watches without a word: the same water raised and returned until it runs clear.

### The ritual

A row of `n` moonflower leaves is numbered 0 to `n-1` from left to right. `dew[i]` is the number of dewdrops on leaf `i` at dusk.

One round of wind works like this:

* All comparisons use the counts at the start of the round.
* For every leaf `i` from 0 to `n-2`, if `dew[i]` is greater than `dew[i+1]`, exactly one drop moves from leaf `i` to leaf `i+1`.
* All such moves happen at once.
A leaf can receive one drop from its left and give one drop to its right in the same round, and may end the round unchanged.
* If a leaf holds no more drops than the leaf to its right, nothing moves between them.
The rightmost leaf never gives a drop.

The gardeners count `rounds` breaths of wind; after each breath they record the new state.

### What to return

Return an object with two fields:

* `n`: the number of leaves.
* `frames`: a single flat array.
Frame 0 is `dew` as given.
After each round, append the new counts for that round.
The display draws one frame per block of `n` numbers.

The number of leaves `n` is from 3 to 8.
Each entry of `dew` is between 0 and 20. `rounds` is between 0 and 14.
"""
import unittest

def silentRounds(dew, rounds):
    """`record(...)` the initial bars, then apply each round, recording the bars after it."""
    n = len(dew)
    frames = dew.copy()
    for _ in range(rounds):
        next_dew = [dew[0]]
        for a, b in zip(dew, dew[1:]):
            if a > b:
                next_dew[-1] -= 1
                b += 1
            next_dew.append(b)
        dew = next_dew
        frames.extend(dew)
    return {"n": n, "frames": frames}

class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(silentRounds([2, 0, 1], 2), {"n": 3, "frames": [2, 0, 1, 1, 1, 1, 1, 1, 1]})
        self.assertEqual(silentRounds([3, 2, 1, 0], 3), {"n": 4, "frames": [3, 2, 1, 0, 2, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2]})
        self.assertEqual(silentRounds([4, 0, 4, 0, 4, 0, 4, 0], 1), {"n": 8, "frames": [4, 0, 4, 0, 4, 0, 4, 0, 3, 1, 3, 1, 3, 1, 3, 1]})

if __name__ == "__main__":
    unittest.main()
