"""Fleet Dispatch

A courier dispatch center has a fleet of numTrucks identical trucks.
A line of packages waits to be delivered, each represented by an integer number of minutes in deliveryTimes.
The packages must be processed in the given order; as soon as a truck becomes free, it takes the next waiting package and is busy for that many minutes.

Return the earliest time (in minutes) when every package is out for delivery.

## Constraints

* `1 ≤ deliveryTimes.length ≤ 500`
* `1 ≤ deliveryTimes[i] ≤ 1,000,000`
* `1 ≤ numTrucks ≤ 200`
"""

import heapq

def minCompletionTime(deliveryTimes, numTrucks):
    """Return earliest finish time."""
    completion = deliveryTimes[:numTrucks]
    heapq.heapify(completion)
    for i in deliveryTimes[numTrucks:]:
        heapq.heappush(completion, i + heapq.heappop(completion))
    return max(completion)

assert minCompletionTime([3, 2, 5], 2) == 7
assert minCompletionTime([4, 4, 4], 3) == 4
assert minCompletionTime([1, 2, 3, 4, 5], 5) == 5
assert minCompletionTime([10], 1) == 10
