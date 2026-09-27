"""Reading the Reel

An archive keeps its catalog on a reel of frames.
Each frame carries one label: `0` for an ordinary entry, `1` for a start marker, and `2` for an end marker.
A clerk may start reading at any start-marker frame, then reads consecutive frames until the first end-marker frame, which is included in the read.

You are given the array `frames`; `frames[i]` is the label of frame `i`.
Return the number of frames in the longest readable run.
If no end marker follows any start marker, return `0`.

The reel holds `n` frames, with `0 <= n <= 200`, and every frame's label is one of `0`, `1`, or `2`.
"""
import unittest

ORDINARY, START, END = range(3)

def archiveReel(frames):
    """Return the longest readable run."""
    best = 0
    start = None
    for i, frame in enumerate(frames):
        if frame == START and start is None:
            start = i
        if frame == END and start is not None:
            best = max(best, i - start + 1)
            start = None
    return best

class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(archiveReel([0, 1, 0, 0, 2, 0]), 4)
        self.assertEqual(archiveReel([1, 0, 2]), 3)
        self.assertEqual(archiveReel([2, 0, 0, 1, 0, 0, 2]), 4)

if __name__ == "__main__":
    unittest.main()
