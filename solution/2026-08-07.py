"""The Listening Post

The night shift at a deep-space listening post begins with the beacon log.
Entry i says a beacon is transmitting on radio channel `channels[i]` at signal power `powers[i]`; several beacons can share one channel, and a locked channel records all of them at once.

Before dawn you may lock the receiver onto as many channels as you like, and the night's haul is the combined power of every beacon on a locked channel.
The receiver's filters are wide, though: a locked channel drowns out both channel numbers next to it, so two channels whose numbers differ by exactly 1 can never both be locked.
Channels further apart never interfere, and a channel nobody transmits on is worth nothing.

Return the largest total power one night can record.

Constraints: `1 <= n <= 200`, where `n` is the length of `channels`, with `powers` always the same length, `1 <= channels[i] <= 200`, and `1 <= powers[i] <= 1000`.
"""
import collections
import functools

def maxRecordedPower(channels, powers):
    """Return the largest total power one night can record."""
    values = collections.defaultdict(int)
    for channel, power in zip(channels, powers):
        values[channel] += power

    vals = sorted(values.items())
    num = len(vals) - 1
    
    @functools.cache
    def get_max(idx: int) -> int:
        if idx > num:
            return 0
        if idx == num:
            return vals[idx][1]
        if vals[idx + 1][0] - vals[idx][0] > 1:
            return vals[idx][1] + get_max(idx + 1)
        return max(vals[idx][1] + get_max(idx + 2), get_max(idx + 1))

    return get_max(0)

assert maxRecordedPower([2, 5, 2, 6], [4, 7, 3, 5]) == 14
assert maxRecordedPower([8, 9], [6, 10]) == 10
assert maxRecordedPower([1, 2, 3, 4, 5], [3, 3, 3, 3, 3]) == 9
