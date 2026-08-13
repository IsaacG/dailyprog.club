"""The Rehearsal Lights

The company rehearses on a bare floor chalked into squares, `rows` rows deep and `cols` squares across.

Strung above it is a lattice of light strips, one strip over every row of squares and one over every column.
The electrician plugs lamps in at crossings of that lattice.
The lamps are given as `lampRows` and `lampCols`, two lists of the same length: lamp j hangs over the square in row `lampRows[j]` and column `lampCols[j]`, counting rows and columns from 0.
Plugging a lamp in feeds current to both strips it touches, so every square along that row and every square along that column is lit.
Nothing else feeds the lattice, and two lamps may be plugged in over the same square.

The director wants to know how much of the floor she cannot use.
Return how many squares get no light at all.

Constraints:

* `1 <= rows <= 30000` and `1 <= cols <= 30000`
* `0 <= m <= 200`, where `m` is the number of lamps
* `lampRows` and `lampCols` both hold `m` entries
* each entry of `lampRows` is from 0 to `rows - 1`, and each entry of `lampCols` is from 0 to `cols - 1`
"""

def darkPanels(rows, cols, lampRows, lampCols):
    "Return how many squares get no light at all."
    total = rows * cols
    lit = cols * len(set(lampRows)) + rows * len(set(lampCols)) - len(set(lampRows)) * len(set(lampCols))
    return total - lit

assert darkPanels(4, 5, [0, 2], [1, 3]) == 6
assert darkPanels(3, 3, [1], [1]) == 4
assert darkPanels(6, 4, [0, 3, 5], [0, 1, 2]) == 3
