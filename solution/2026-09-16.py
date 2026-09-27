"""What the Roots Leave

The Maker gathered the waters under the sky and called them Seas, and the earth brought forth the first tree, bearing fruit with seed in it, according to its kind.

When rain soaks the earth above the first tree it sinks down through the roots, and whatever the roots do not drink seeps on beneath them to the Seas.
Return `answer`, the measures of water that reach the Seas (0 when the roots drink it all), and `visited`, the numbers of the roots the water enters, in order, starting with root 0.

The tree has `n` roots in rows: one at the surface, two forking from it beneath, and so on, each row twice as wide as the last.
Numbered row by row from the surface, left to right, from 0, root `k` forks into root `2k + 1` (down-left) and root `2k + 2` (down-right); the lowest row holds the root tips, with nothing beneath.
Every root can hold `holds` measures, and `soaked[i]` is what root `i` holds before the rain.

`rain` measures sink into root 0.
Each root the water enters drinks until it is full or the water runs out.
What is left is drawn into the drier of the two roots forking beneath, the one holding less; when both hold the same, it goes to the left.
Water left after a root tip has nowhere to go but the Seas.

Constraints:

* `n` is 3, 7, or 15, where `n` is the number of roots in `soaked` (every root has either two roots forking from it or none)
* `1 <= holds <= 9`
* `0 <= soaked[i] <= holds`, so no root ever holds more than 9
* `1 <= rain <= 40`
"""
import unittest


def rootsDrink(soaked, holds, rain):
    """Return the path of roots water enters, root 0 first; set answer to what reaches the Sea."""
    node, visited = 0, []
    while node < len(soaked) and rain:
        visited.append(node)
        rain = max(0, rain - holds + soaked[node])
        node = node * 2 + 1
        if node < len(soaked) and soaked[node + 1] < soaked[node]:
            node += 1

    return {"answer": rain, "visited": visited}


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(rootsDrink([2, 1, 4, 3, 0, 5, 2], 5, 15), {"answer": 3, "visited": [0, 1, 4]})
        self.assertEqual(rootsDrink([0, 3, 3, 4, 4, 1, 2], 4, 9), {"answer": 4, "visited": [0, 1, 3]})
        self.assertEqual(rootsDrink([3, 2, 1], 3, 5), {"answer": 3, "visited": [0, 2]})

if __name__ == "__main__":
    unittest.main()
