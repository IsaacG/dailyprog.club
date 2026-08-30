"""The Breathing Bed

On the fourth night of the waxing moon, a patch of shadow-moss creeps over the central bed of the Moon Garden.
Elder Thorne and Brother Moss work through the night, peeling the moss back with their bare hands.
Elder Thorne only says that every Work must pass through its blackening before it can breathe.
Elder Thorne records the struggle in the array `events`, where each entry is a single deed: `1` means another dark layer of moss settled over the soil, and `-1` means a layer was peeled back.
The bed starts free of moss, and each peel removes one existing layer.

The soil is smothered if the gardeners ever peel when no layer remains, or if any layer is still covering the soil at dawn.
Return `true` if the bed is breathing freely at the end, `false` otherwise.
An empty `events` means the bed was never covered and counts as breathing freely.

Constraints: 0 <= n <= 10, where `n` is the length of `events`, and each entry is either 1 or -1.
"""
import unittest

def soilBreathes(events):
    """Return if the bed is breathing freely."""
    s = 0
    for e in events: 
        s += e
        if s < 0:
            return False
    return s == 0

class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(soilBreathes([1, -1, 1, -1]), True)
        self.assertEqual(soilBreathes([1, 1, -1, -1]), True)
        self.assertEqual(soilBreathes([1, 1, -1]), False)
        self.assertEqual(soilBreathes([-1]), False)
        self.assertEqual(soilBreathes([]), True)

if __name__ == "__main__":
    unittest.main()
