"""The Radio Operator's Squelch Loop

A radio operator watches a row of signal tones, each written as a lowercase letter.
Whenever `groupSize` identical tones sit side by side, those `groupSize` tones are squelched out (a longer run of one tone loses `groupSize` of its tones), and the tones on either side close the gap.
This repeats until no such run remains.
Given the string `sequence` of tone letters and the integer `groupSize`, return the final row of tones after every squelch.
The outcome is the same regardless of which qualifying runs you squelch first.

### Constraints

* the length of `sequence` is from 0 to 30 inclusive
* `groupSize` is from 2 to 5 inclusive
"""
import unittest

def reduceGroups(sequence, groupSize):
    """Return the letters left after the deletions."""
    changed = True
    while changed:
        out, i, changed = [], 0, False
        while i < len(sequence):
            if i + groupSize > len(sequence) or any(sequence[i] != j for j in sequence[i + 1: i + groupSize]):
                out.append(sequence[i])
                i += 1
            else:
                changed = True
                i += groupSize
        sequence = "".join(out)
    return sequence


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(reduceGroups("aabbcdee", 2), "cd")
        self.assertEqual(reduceGroups("abba", 2), "")
        self.assertEqual(reduceGroups("aa", 3), "aa")
        self.assertEqual(reduceGroups("aaaaa", 2), "a")
        self.assertEqual(reduceGroups("aabbaabbaabbaabbaabbaabbaabbaa", 2), "")

if __name__ == "__main__":
    unittest.main()
