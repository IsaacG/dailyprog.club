"""Level the Crates

At a market, crates are stacked in piles of different heights. `piles[i]` is the number of crates in pile i. In one move, a porter can add one crate to any pile or remove one crate from any pile. The stallholder wants every pile to be exactly the same height. Return the minimum number of moves needed.

The final common height may be any whole number. A pile may be emptied down to zero, but never below zero.

Constraints: `1 <= n <= 5000`, where `n` is the length of `piles`, and each `piles[i]` is an integer in `[0, 10^9]`.
"""
import collections

def levelCrates(piles):
    """Return the minimum number of moves to make every pile the same height."""
    c = collections.deque(list(i) for i in sorted(collections.Counter(piles).items()))
    print(c)

    moves = 0
    while len(c) > 1:
        if c[0][1] < c[-1][1]:
            height, count = c.popleft()
            moves += (c[0][0] - height) * count
            c[0][1] += count
        else:
            height, count = c.pop()
            moves += (height - c[-1][0]) * count
            c[-1][1] += count

    return moves


assert levelCrates([1, 2, 3, 4, 5]) == 6
assert levelCrates([4, 4, 4]) == 0
assert levelCrates([7, 0]) == 7
