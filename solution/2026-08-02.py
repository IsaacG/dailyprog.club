"""The Long Dry Stretch

After a sudden desert storm, a thin canyon is dotted with pools of trapped rainwater.
You are the caravan's water scout.
The canyon is a row of rock columns of different heights, and rain has settled in every dip where taller columns block the flow.
For each column, the water depth resting on it is the smaller of the tallest column to its left and the tallest column to its right, minus the column's own height; if that value is negative, the column holds nothing.
Find the total barrels of water stranded in the whole canyon.

Return an object with three fields:

* answer: the total barrels of water.
* lo: the left scout's index at the start of every step.
* hi: the right scout's index at the same moment.

## How the scouts walk

Start with the left scout at index 0 and the right scout at the last index.
Keep two running records: the tallest column seen so far from the left, and the tallest column seen so far from the right.

* Compare the two columns the scouts currently stand on.
* If the left column is strictly shorter, the left scout takes one step to the right.
  If that column is lower than the tallest seen from the left, credit tallestLeft - height to the total; otherwise just update tallestLeft.
* Otherwise (the right column is shorter or equal), the right scout takes one step to the left, using the mirrored rule with tallestRight.

Record (lo, hi) at the start of every step. Stop when the two scouts reach the same column.

The canyon has between 2 and 10 columns, each height between 0 and 9.
"""

def countStrandedWater(heights):
    """Return answer plus per-step lo and hi index arrays."""
    answer = 0
    lo, hi = 0, len(heights) - 1
    loMax, hiMax = heights[lo], heights[hi]
    los, his = [], []
    while lo < hi:
        los.append(lo)
        his.append(hi)
        if heights[lo] < heights[hi]:
            lo += 1
            if loMax > heights[lo]:
                answer += loMax - heights[lo]
            else:
                loMax = heights[lo]
        else:
            hi -= 1
            if hiMax > heights[hi]:
                answer += hiMax - heights[hi]
            else:
                hiMax = heights[hi]
    return dict(answer=answer, lo=los, hi=his)

assert countStrandedWater([3, 0, 2, 0, 4]) == {"answer": 7, "lo": [0, 1, 2, 3], "hi": [4, 4, 4, 4]}
assert countStrandedWater([2, 0, 2]) == {"answer": 2, "lo": [0, 0], "hi": [2, 1]}
assert countStrandedWater([0, 0, 0, 0]) == {"answer": 0, "lo": [0, 0, 0], "hi": [3, 2, 1]}
