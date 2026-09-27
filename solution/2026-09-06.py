"""The Rotating Course

At a conveyor-belt sushi bar, `plates[i]` is the name of the dish sitting at station i when the belt starts.
Each round, the dish at station i is carried to station `belt[i]`, and all dishes move at the same time. `belt` contains every station index exactly once, so after every round each station receives exactly one dish.

After exactly `rounds` rounds, return an array whose element i is the dish name now sitting at station i.
Dish names are distinct.

Constraints: the number of stations `n` (the length of both `plates` and `belt`) is between 1 and 30, each `belt[i]` is an integer from 0 to n - 1 with each such value appearing once, and `rounds` is an integer from 0 to 10^9.
"""
import unittest

def afterRounds(plates, belt, rounds):
    """Return the dish name now at every station after `rounds` rounds."""
    n = len(belt)
    rbelt = [None] * n
    for a, b in enumerate(belt):
        rbelt[b] = a
    plates = tuple(plates)
    history = [plates]
    seen = {plates}
    i = -1
    for i in range(rounds):
        plates = tuple(plates[rbelt[i]] for i in range(n))
        print(i, plates)
        if plates in seen:
            break
        seen.add(plates)
        history.append(plates)
    if i == rounds - 1:
        return list(plates)
    return list(history[rounds % (i + 1)])


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(afterRounds(["maki", "sake", "tamago", "uni", "ebi"], [1, 2, 3, 4, 0], 1), ["ebi", "maki", "sake", "tamago", "uni"])
        self.assertEqual(afterRounds(["a", "b"], [1, 0], 0), ["a", "b"])
        self.assertEqual(afterRounds(["maki", "sake", "tamago", "uni"], [1, 0, 3, 2], 3), ["sake", "maki", "uni", "tamago"])
        self.assertEqual(afterRounds(["a", "b", "c"], [1, 2, 0], 4), ["c", "a", "b"])

if __name__ == "__main__":
    unittest.main()
