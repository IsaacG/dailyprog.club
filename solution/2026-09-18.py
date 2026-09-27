"""Birds of a Kind

The Maker said, let the waters teem with living creatures, and let birds fly above the earth across the expanse of the sky; and there was evening and there was morning, the fifth day.

The birds crossed the sky in one long line. `birds` lists them from head to tail: `birds[i]` is the kind of the bird in place i, a word such as `gull` or `heron`.

Split the line into flocks.
Each flock is an unbroken stretch of the line, and all birds of the same kind must end up in the same flock; a flock may hold several kinds.
Split the line into as many flocks as that rule allows, then return the number of birds in the flock that holds `kind`, or 0 if no bird in the line is of that kind.

For example, the line `gull tern gull crane tern dove` splits no finer than `gull tern gull crane tern | dove`: the gulls and the terns overlap, so they hold the first five birds together.
Asked about `gull`, return 5.

Constraints: `1 <= n <= 1000`, where `n` is the number of birds in `birds`; each kind in the line, and `kind` itself, is a word of 2 to 10 lowercase letters.
"""
import unittest

def flockOfKind(birds, kind):
    """Return the number of birds in the flock that carries the kind, or 0 if no bird is of that kind."""
    start, end = {}, {}
    for i, bird in enumerate(birds):
        start.setdefault(bird, i)
        end[bird] = max(i, end.get(bird, i))
    if kind not in start:
        return 0
    i, j = start[kind], end[kind]
    todo = set(start) - {kind}
    while todo:
        bird = next(( bird for bird in todo if start[bird] < j and end[bird] > i), None)
        if bird is None:
            break
        i, j = min(i, start[bird]), max(j, end[bird])
        todo.remove(bird)
    return j - i + 1


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(flockOfKind(["gull", "tern", "gull", "crane", "tern", "dove"], "gull"), 5)
        self.assertEqual(flockOfKind(["gull", "tern", "gull", "crane", "tern", "dove"], "dove"), 1)
        self.assertEqual(flockOfKind(["heron", "heron", "stork"], "wren"), 0)
        self.assertEqual(flockOfKind(["dove", "crane", "dove", "crane", "lark", "crane", "lark"], "dove"), 7)
        self.assertEqual(flockOfKind(["tern", "gull", "tern", "gull", "dove"], "gull"), 4)

if __name__ == "__main__":
    unittest.main()
