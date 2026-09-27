"""The Bindery's Cutting Order

A bookbinder receives a strip of printed cloth and must slice it into contiguous panels.
Each character on the strip is a dye lot, and a lot may not appear on two different panels, or the colours will not match when the book is bound.

Given `text`, a strip of characters where `text[i]` is the dye lot printed at position i, cut the strip into contiguous panels that together cover the whole strip, so that each dye lot appears on at most one panel, and so that the number of panels is as large as possible.
Return the lengths of those panels in the order they appear.
An empty strip produces no panels.

### Constraints

* 0 <= n <= 40, where n is the number of characters in `text`.
"""
import unittest

def partLengths(text):
    """Return the lengths of the panels, in order."""
    start, end = {}, {}
    for i, char in enumerate(text):
        start.setdefault(char, i)
        end[char] = max(i, end.get(char, i))

    lengths = []
    todo = set(start)
    cur_start, cur_end = 0, 0
    while cur_end < len(text):
        char = next((char for char in todo if start[char] <= cur_end), None)
        if char is None:
            lengths.append(cur_end - cur_start + 1)
            cur_start = cur_end + 1
            cur_end = cur_start
        else:
            todo.remove(char)
            cur_end = max(cur_end, end[char])
    return lengths


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(partLengths("aabbc"), [2, 2, 1])
        self.assertEqual(partLengths("abac"), [3, 1])
        self.assertEqual(partLengths("abab"), [4])
        self.assertEqual(partLengths("abcde"), [1, 1, 1, 1, 1])
        self.assertEqual(partLengths("z"), [1])
        self.assertEqual(partLengths("abcdefghijklmnopqrstuvwxyzabcdefghijklmn"), [40])

if __name__ == "__main__":
    unittest.main()
