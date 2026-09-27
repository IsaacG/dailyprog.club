"""The Archivist's Return Cart

A library clerk clears the return cart one stack at a time.
The cart is a platform that can hold at most `limit` units of book weight.
The books are handled in the order they appear in the list `weights`, where `weights[i]` is the weight of the i-th book.
No book is heavier than `limit`, so every book ends up on the cart.

Each book is handled in order:

1.
While the cart is not empty and the cart's total weight plus the arriving book's weight is greater than `limit`, the book currently on top of the cart is lifted off and set aside, and this repeats until the arriving book would fit.
2.
Then the arriving book is set on top of the cart.

Each of those two actions is a move, recorded in the order it happens: the label `"push"` when a book is set on the cart, and the label `"pop"` when the top book is lifted off.

Return an object with three fields. `ops` is the list of labels, one per move. `values` is parallel to `ops`: for a `"push"` it is the weight of the book set down, for a `"pop"` it is the weight of the book lifted off, that is, the book that was on top at that moment. `answer` is the largest number of books that stood on the cart at any one moment.

The cart is empty before the first move, `ops` and `values` always have the same length and at least one entry, and no book is ever lifted off an empty cart.

### Constraints

* 3 <= n <= 5, where `n` is the number of books.
* 1 <= `weights[i]` <= 12 for each book.
* 1 <= `limit` <= 15.
"""
import unittest

def pileMoves(weights, limit):
    """Replay the world's moves, recording each one ("push"/"pop" + its value); set answer."""
    ops, values, stack = [], [], []
    answer, cur = 0, 0
    for weight in weights:
        while cur + weight > limit:
            ops.append("pop")
            removed = stack.pop()
            values.append(removed)
            cur -= removed
        ops.append("push")
        values.append(weight)
        stack.append(weight)
        cur += weight
        answer = max(answer, len(stack))
    return {"answer": answer, "ops": ops, "values": values}


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(pileMoves([5, 3, 4, 6], 10), {"answer": 2, "ops": ["push", "push", "pop", "push", "pop", "pop", "push"], "values": [5, 3, 3, 4, 4, 5, 6]})
        self.assertEqual(pileMoves([1, 2, 3], 10), {"answer": 3, "ops": ["push", "push", "push"], "values": [1, 2, 3]})
        self.assertEqual(pileMoves([4, 4, 4], 4), {"answer": 1, "ops": ["push", "pop", "push", "pop", "push"], "values": [4, 4, 4, 4, 4]})
        self.assertEqual(pileMoves([6, 2, 5, 3], 8), {"answer": 2, "ops": ["push", "push", "pop", "pop", "push", "push"], "values": [6, 2, 2, 6, 5, 3]})
        self.assertEqual(pileMoves([1, 1, 1, 2, 5], 5), {"answer": 4, "ops": ["push", "push", "push", "push", "pop", "pop", "pop", "pop", "push"], "values": [1, 1, 1, 2, 2, 1, 1, 1, 5]})

if __name__ == "__main__":
    unittest.main()
