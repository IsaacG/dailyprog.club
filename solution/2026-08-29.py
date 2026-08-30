"""The One-Way Wing

Vera has the floor plan of the Aldermont Museum's east wing memorized: a rectangle of rooms, and every service door in it swings one way only, east or south.
Tonight she slips in through the northwest corner room, and the vault waits in the southeast corner.

Every room on the way works on her nerve.
The wing has `width` rooms in each row, and the array `rooms` lists the whole floor row by row starting from the northwest, so the room in row r and column c (both counted from 0) is entry `rooms[r * width + c]`.
A negative entry is a patrol post or a creaking passage that costs her that much nerve the moment she steps in; a positive entry is a dark, quiet gallery where she steadies herself and wins that much back; a 0 leaves her unchanged.

Her nerve must stay at 1 or higher through every room she enters, the corner room where she starts and the vault itself included; if it ever falls below 1 she abandons the job on the spot.
From any room she may continue only to the room directly east or the room directly south, and she plans her whole route before the night begins.

Return the smallest whole number of nerve Vera can start the night with and still reach the vault.

### Constraints

* 1 <= `width` <= 12, where `width` is the number of rooms in each row.
* `n` is the number of entries in `rooms`, with 1 <= n <= 144.
The floor is always a full rectangle: n splits evenly into rows of `width`, with at most 12 rows.
* Each entry of `rooms` is between -30 and 30.
"""
import unittest
import functools

def minimumNerve(rooms, width):
    """Return the smallest starting nerve that reaches the vault."""
    height = len(rooms) // width
    rooms = {
        (x, y): rooms[x + y * width]
        for y in range(height)
        for x in range(width)
    }
    end = (width - 1, height - 1)

    @functools.cache
    def needed(x: int, y: int) -> int:
        if (x, y) == (width - 1, height - 1):
            return max(1, 1 - rooms[x, y])
        this_room = max(1, 1 - rooms[x, y])
        needed_next = [
            needed(x + dx, y + dy) - rooms[x, y]
            for dx, dy in [(1, 0), (0, 1)]
            if (x + dx, y + dy) in rooms
        ]
        return max(this_room, min(needed_next, default=this_room))

    return needed(0, 0)


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(minimumNerve([-3, 4, -2, 2, -6, 1, -1, 3, -2], 3), 4)
        self.assertEqual(minimumNerve([0, 3, 1, 2], 2), 1)
        self.assertEqual(minimumNerve([-2, 3, -4, 1], 4), 4)
        self.assertEqual(minimumNerve([-2], 1), 3)

if __name__ == "__main__":
    unittest.main()
