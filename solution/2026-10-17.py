"""The Roundabout Routes

A city planner maps a network of two-way streets as pairs of intersections in `links`.
Each pair `links[2*i]` and `links[2*i+1]` are the two ends of one street.
A roundabout route is a sequence of three or more distinct intersections where each consecutive pair, including the last and first, is connected by a street.
An intersection is on a roundabout route if at least one such route passes through it.
Return how many of the `n` intersections lie on at least one roundabout route.

### Constraints

* `n` is at least 1.
* The length of `links` is between 0 and 20.
* Each endpoint is an integer from 0 to `n` - 1.
"""
import unittest

import collections
import itertools

def countLoopedPoints(n, links):
    # TODO: return how many of the n points lie on at least one loop
    conns = collections.defaultdict(set)
    for a, b in itertools.batched(links, n=2):
        conns[a].add(b)
        conns[b].add(a)
    print(conns)

    def loops(cur, via, prior):
        got = set()
        next_via = via + (cur,)
        for conn in conns[cur]:
            if conn == prior:
                continue
            if conn in via:
                p = via[via.index(conn):]
                got.update(p)
                print(f"Found loop @ {cur}-{conn}, {p=}")
            else:
                got.update(loops(conn, next_via, cur))
        return got

    todo = set(conns)
    out = set()
    while todo:
        n = todo.pop()
        out.update(loops(n, tuple(), n))
    return len(out)


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(countLoopedPoints(7, [0, 1, 1, 2, 2, 3, 3, 0, 2, 4, 4, 5]), 4)
        self.assertEqual(countLoopedPoints(7, [0, 1, 1, 2, 2, 0, 3, 4, 4, 5, 5, 3, 0, 6, 6, 3]), 6)
        self.assertEqual(countLoopedPoints(6, [0, 1, 1, 2, 2, 3, 4, 5]), 0)
        self.assertEqual(countLoopedPoints(6, [0, 1, 2, 3, 4, 0]), 0)
        self.assertEqual(countLoopedPoints(4, [0, 1, 2, 1, 2, 0]), 3)
        self.assertEqual(countLoopedPoints(5, [0, 1, 1, 2, 2, 3, 3, 0, 0, 2]), 4)
        self.assertEqual(countLoopedPoints(1, []), 0)
        self.assertEqual(countLoopedPoints(12, [0, 1, 1, 2, 2, 3, 3, 4, 4, 0, 5, 6, 6, 7, 7, 5, 4, 8, 8, 9]), 8)

if __name__ == "__main__":
    unittest.main()
