"""Rush Hour Under the Mountain

A mountain tunnel runs one way, and several vehicles can be inside it at the same time.
The safety log is a flat list of numbers called `entries`: for vehicle i, `entries[2*i]` is the minute it enters the tunnel and `entries[2*i+1]` is the minute it clears the tunnel.

A vehicle is inside the tunnel for every minute from its entry minute up to but not including its clearing minute, so at its clearing minute it is already out and another vehicle may be inside then.

Write a function that returns the numbers of the vehicles that are inside the tunnel at the busiest minute, that is, the minute with the most vehicles inside.
Vehicles are numbered from 0 in the order their pairs appear in `entries`.
If several minutes tie for busiest, use the earliest of them.
Return those vehicle numbers in increasing order.

### Constraints

* `entries` holds an even number of values `n`, with 2 <= n <= 20, so there are between 1 and 10 vehicles.
* Every value is a whole minute between 0 and 1440.
* Each vehicle's clearing minute is greater than its entry minute.
"""
import unittest

# Adapted from 2026-07-03
def vehiclesAtBusiest(entries):
    """Return the vehicle numbers inside the tunnel at the busiest minute, in increasing order."""
    starts = sorted(((e, i) for i, e in enumerate(entries[0::2])), reverse=True)
    ends = sorted(((e, i) for i, e in enumerate(entries[1::2])), reverse=True)

    active = set()
    mostIdxs = set()
    while starts:
        cur = starts[-1][0]
        while ends and ends[-1][0] <= cur:
            active.remove(ends.pop()[1])
        while starts and starts[-1][0] <= cur:
            active.add(starts.pop()[1])
        if len(active) > len(mostIdxs):
            mostIdxs = active.copy()
    return sorted(mostIdxs)



class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(vehiclesAtBusiest([0, 3, 2, 6, 5, 8]), [0, 1])
        self.assertEqual(vehiclesAtBusiest([0, 1, 5, 6]), [0])
        self.assertEqual(vehiclesAtBusiest([7, 9]), [0])
        self.assertEqual(vehiclesAtBusiest([0, 10, 1, 11, 2, 12]), [0, 1, 2])

if __name__ == "__main__":
    unittest.main()
