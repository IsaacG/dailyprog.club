"""Down the Old Oak

First frost is coming, and a squirrel is filling her cheeks on the way down the old oak.
Return `answer`, the total number of acorns she gathers before settling in for the winter, and `visited`, the hollows she empties, in order.

The oak has `n` hollows arranged in rows: one at the crown, two in the row beneath it, and so on, each row twice as wide as the one above.
The hollows are numbered row by row from the crown, left to right, starting at 0, so beneath hollow `k` sit hollow `2k + 1` (down-left) and hollow `2k + 2` (down-right).
Hollows in the lowest row have nothing beneath them. `hollows` lists every stash: `hollows[i]` is the number of acorns stored in hollow `i`.

She starts at the crown, hollow 0, and empties it; she is already there, so she takes that stash no matter how small it is.
Then, again and again:

* If her hollow is in the lowest row, she settles in where she is.
* Otherwise she peers into the two hollows beneath her and picks the fuller one; if they hold the same amount, she picks the down-left one.
* If the hollow she picked holds at least `least` acorns, she climbs down into it and empties it.
Any less is not worth the climb: she settles in where she is.

`visited` records the numbers of the hollows she empties, in order, starting with the crown; `answer` counts every acorn she gathered.

Constraints:

* `n` is 3, 7, or 15, where `n` is the number of hollows (every hollow has either two hollows beneath it or none)
* `0 <= hollows[i] <= 20`
* `1 <= least <= 20`
"""

def acornRun(hollows, least):
    visited = []
    def record(hollow):
        visited.append(hollow)
    answer = 0
    pos = 0
    while True:
        record(pos)
        answer += hollows[pos]
        pos = 2 * pos + 1 
        if pos >= len(hollows):
            break
        if hollows[pos + 1] > hollows[pos]:
            pos += 1
        if hollows[pos] < least:
            break

    return {"answer": answer, "visited": visited}

assert acornRun([4, 2, 5, 9, 1, 3, 6], 3) == {"answer": 15, "visited": [0, 2, 6]}
assert acornRun([5, 4, 4, 7, 2, 9, 9], 2) == {"answer": 16, "visited": [0, 1, 3]}
assert acornRun([6, 1, 2], 4) == {"answer": 6, "visited": [0]}
