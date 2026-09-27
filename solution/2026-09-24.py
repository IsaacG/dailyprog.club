"""Tech Rehearsal Call Sheet

A stage manager schedules a tech rehearsal in rounds.
Every act in `items` must finish its rehearsal before the show can open.
The `rules` list holds names read as consecutive pairs: the name at an even index must finish before the name at the next index may begin, so the first name in a pair precedes the second, the third precedes the fourth, and so on.
Every name in `rules` also appears in `items`.

### Rounds

In each round, every act whose prerequisites have all finished before the round starts is rehearsed, and all of those acts finish together at the end of that round.
Any number of acts may be rehearsed in the same round, and an act with no prerequisites is rehearsed in round 1.

The pairs never contradict each other: no act is required, directly or indirectly, to finish before itself.

Return the number of rounds needed to finish every act.

### Constraints

* 2 <= number of items <= 10
* 0 <= number of rules <= 20, and the number of rules is even
* Names are distinct non-empty strings
"""
import unittest

import collections
import itertools

def countRounds(items, rules):
    """Return the number of rounds needed to finish every item."""
    prereqs = collections.defaultdict(set)
    for a, b in itertools.batched(rules, 2):
        prereqs[b].add(a)
    todo = set(items)
    done = set()
    rounds = 0
    while todo:
        rounds += 1
        can_do = {i for i in todo if done >= prereqs[i]}
        done |= can_do
        todo -= can_do
    return rounds


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(countRounds(["alpha", "beta", "gamma", "delta"], ["alpha", "beta", "beta", "delta", "alpha", "gamma", "gamma", "delta"]), 3)
        self.assertEqual(countRounds(["alpha", "beta"], []), 1)
        self.assertEqual(countRounds(["delta", "gamma", "beta", "alpha"], ["alpha", "beta", "beta", "gamma", "gamma", "delta"]), 4)
        self.assertEqual(countRounds(["alpha", "beta", "gamma", "delta"], ["alpha", "beta", "gamma", "delta"]), 2)
        self.assertEqual(countRounds(["alpha", "beta", "gamma"], ["alpha", "beta", "beta", "gamma"]), 3)
        self.assertEqual(countRounds(["alpha", "beta", "gamma", "delta"], ["alpha", "beta", "beta", "gamma", "delta", "gamma"]), 3)
        self.assertEqual(countRounds(["kappa", "iota", "theta", "eta", "zeta", "epsilon", "delta", "gamma", "beta", "alpha"], ["alpha", "beta", "zeta", "eta", "beta", "gamma", "eta", "theta", "gamma", "delta", "iota", "kappa", "delta", "epsilon", "alpha", "zeta", "theta", "iota", "epsilon", "kappa"]), 6)

if __name__ == "__main__":
    unittest.main()
