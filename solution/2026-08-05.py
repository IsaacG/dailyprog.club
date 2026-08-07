"""The Tilted Pin Board

A bagatelle board stands in the toymaker's workshop: a square frame of `n` by `n` squares, propped so it leans a little to the right. Brass pins are driven into some of the squares. A glass bead is set into the top row, let go, and clatters down to the catch tray along the bottom edge.

Report the bead's whole run: `rows`, `cols`, and `dirs`, one entry per step, where index `0` is the moment it is let go. `rows[i]` and `cols[i]` are the square it occupies (both counted from 0, rows from the top and columns from the left), and `dirs[i]` is `"down"` if it fell into that square (and for the moment it was let go), or `"right"` or `"left"` if it rolled there.

### The board

`pins` lists the squares row by row, left to right: `1` for a square holding a pin, `0` for a bare square. The top row never holds a pin. The bead is let go in the top row, in column `startCol`, and at that moment it counts as falling.

### How the bead moves

Each step the bead does exactly one thing:

* If it is in the bottom row, it has arrived at the tray and the run is over.
* Otherwise, if the square directly below it is bare, the bead drops into that square, and is falling again.
* Otherwise a pin is holding the bead up, and it rolls sideways within its own row:
* A bead that reached its square by falling, or by rolling **right**, follows the lean and rolls into the square on its right. If that square is off the frame or holds a pin, the bead is shoved into the square on its **left** instead. If that square is off the frame or holds a pin too, the bead is wedged and the run is over.
* A bead that reached its square by going **left** keeps going left: while a pin holds it up it only ever tries the square on its left. It does not turn back with the lean. When that square is off the frame or holds a pin, the bead is wedged and the run is over.

A bead forgets a shove only by falling: the moment it drops into a bare square it is falling again, so the lean takes over at the next pin it meets.

One roll with the lean (`b` is the bead, `o` a pin):

```
before        after
. b . .       . . b .
. o . .       . o . .
```

### Constraints

* 3 <= `n` <= 6
* `pins` has exactly `n * n` entries, each 0 or 1
* 0 <= `startCol` <= `n` - 1
"""
def beadDrop(n, startCol, pins):
    x, y = startCol, 0
    rows, cols, dirs = [0], [x], ["down"]
    space = {(x, y) for y in range(n) for x, pin in enumerate(pins[y * n:(y + 1) * n]) if pin == 0}
    right = True
    while y < n - 1:
        if (x, y + 1) in space:
            dirs.append("down")
            right = True
            y += 1
        elif right and (x + 1, y) in space:
            dirs.append("right")
            x += 1
        elif (x - 1, y) in space:
            dirs.append("left")
            x -= 1
            right = False
        else:
            break
        cols.append(x)
        rows.append(y)
        
    return {"rows": rows, "cols": cols, "dirs": dirs}

assert beadDrop(4, 1, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]) == {"rows": [0, 1, 1, 2, 3], "cols": [1, 1, 2, 2, 2], "dirs": ["down", "down", "right", "down", "down"]}
assert beadDrop(3, 2, [0, 0, 0, 0, 0, 0, 0, 0, 0]) == {"rows": [0, 1, 2], "cols": [2, 2, 2], "dirs": ["down", "down", "down"]}
assert beadDrop(6, 3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == {"rows": [0, 1, 1, 1, 2, 3, 4, 5], "cols": [3, 3, 2, 1, 1, 1, 1, 1], "dirs": ["down", "down", "left", "left", "down", "down", "down", "down"]}
