"""The Fourth-Floor Corridor

The fourth floor has one corridor, and it is exactly one trolley wide.

At five o'clock the post room lets every mail trolley go at once.
The trolleys stand in a line running from the west end of the corridor to the east end, and `trolleys[i]` is the i-th of them: the number is positive if that trolley was pushed east and negative if it was pushed west, and its size is how many sacks of mail the trolley carries.
Every trolley rolls at the same pace, so two trolleys pushed the same way never meet.

When a trolley rolling east comes up against a trolley rolling west, the corridor is too narrow for both to pass:

* If one of them carries more sacks than the other, that one has right of way.
The lighter trolley's sacks are tipped onto it, so from then on it carries both loads, and the emptied trolley is wheeled into a side room.
* If the two carry the same number of sacks, neither yields.
Both are wheeled into side rooms, and their mail is sent down to the sorting desk.

A trolley that has taken on extra sacks keeps rolling the way it was already going, heavier than it was, and may come up against another trolley further along.

Return the load of every trolley still rolling once no two of them can meet again, listed from the west end to the east end, using the same sign convention.

Constraints:

* `0 <= n <= 200`, where `n` is the number of trolleys
* each entry of `trolleys` is between -1000 and 1000, and is never 0
"""

def settleCorridor(trolleys: list[int]) -> list[int]:
    """Return the load of each trolley still rolling, west to east."""
    prior_len = 0
    while len(trolleys) != prior_len:
        prior_len = len(trolleys)
        i = 0
        while i < len(trolleys) - 1:
            if trolleys[i] < 0 or trolleys[i + 1] > 0:
                i = i + 1
            elif trolleys[i] == -trolleys[i + 1]:
                del trolleys[i:i + 2]
            else:
                trolleys[i] = (trolleys[i] - trolleys[i + 1]) * (1 if trolleys[i] > -trolleys[i + 1] else -1)
                del trolleys[i + 1:i + 2]
    return trolleys

assert settleCorridor([5, -2, 3]) == [7, 3]
assert settleCorridor([-4, 2, -6, 1]) == [-4, -8, 1]
assert settleCorridor([6, -6, 2]) == [2]
