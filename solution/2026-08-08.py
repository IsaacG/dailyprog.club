"""Chalk Lines

The climbing league's team final comes down to the big wall.
The wall is a single row of panels, and panel i takes `times[i]` seconds of climbing to clear.
Your team has `climbers` athletes.

Before the buzzer, the coach chalks dividing lines onto the wall, splitting it into exactly `climbers` sections of consecutive panels, one section per athlete, and every section holds at least one panel.
At the buzzer everyone starts at once, each athlete clearing only their own section, panel after panel.
The team's time is the moment the last athlete tops out.

Return the shortest team time the coach can achieve by placing the chalk lines well.

Constraints: `1 <= climbers <= n <= 200`, where `n` is the length of `times`, and `1 <= times[i] <= 1000`.
"""
import functools

def shortestFinish(times, climbers):
    """Return the shortest possible team time."""

    @functools.cache
    def best(acc, idx, climbers):
        if climbers == 1:
            return sum(times[idx:])
        if idx + climbers == len(times):
            b = max(times[-(climbers - 1):])
            return max(b, acc + times[idx])
        return min(
            max(acc + times[idx], best(0, idx + 1, climbers - 1)),
            best(acc + times[idx], idx + 1, climbers)
        )

    return best(0, 0, climbers)

assert shortestFinish([7, 2, 5, 10, 8], 2) == 18
assert shortestFinish([3, 6, 2, 4], 4) == 6
assert shortestFinish([5, 5, 5, 5, 5, 5], 3) == 10
