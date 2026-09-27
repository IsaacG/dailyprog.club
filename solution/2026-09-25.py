"""Reading the Harbour Signal Mast

A signal mast spells out a short message by hanging one flag per slot.
The flags are hoisted in rows of `width` slots, each row filled left to right, and the last row may be short.
A reading is then taken by calling down each column in turn, from the top of the mast to the bottom, starting with the leftmost column.

You are given `text`, the string of flags read off column by column, and `width`, the number of slots in a full row.
Return the message the mast was spelling.

### Constraints

* `text` has between 1 and 20 characters.
* `width` is between 1 and 8.
* Every row except possibly the last is exactly `width` flags long.
"""
import unittest
import itertools

def readSignalMast(text, width):
    """Return the message the text encodes."""
    short_count, full = divmod(len(text), width)
    long_count = short_count + 1
    first_block = long_count * full
    rows = [
        text[s:s + long_count] for s in range(0, first_block, long_count)
    ] + [
        text[s:s + short_count] for s in range(first_block, len(text), short_count or 1)
    ]
    return "".join("".join(i) for i in itertools.zip_longest(*rows, fillvalue=""))


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(readSignalMast("AFBGCHDIEJ", 5), "ABCDEFGHIJ")
        self.assertEqual(readSignalMast("AEIBFJCGDH", 4), "ABCDEFGHIJ")
        self.assertEqual(readSignalMast("A", 1), "A")
        self.assertEqual(readSignalMast("AIQBJRCKSDLTEMFNGOHP", 8), "ABCDEFGHIJKLMNOPQRST")
        self.assertEqual(readSignalMast("ABC", 5), "ABC")

if __name__ == "__main__":
    unittest.main()
