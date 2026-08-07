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

