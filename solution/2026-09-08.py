"""The Seeding Sheet

The club's autumn open is a straight knockout, and the referee draws the sheet from the seeding list. `players` lists the entrants best first: `players[0]` is the top seed, `players[1]` the second seed, and so on down to the lowest seed.
The number of entrants is a power of two, so nobody sits out a round.

The sheet is one column of names.
Two names written next to each other on the sheet (the first and second, the third and fourth, and so on) meet in the first round.
The winners of two neighbouring first-round matches meet in the second round, the winners of two neighbouring second-round matches meet in the third, and so on up to the final.

```
seed 1 -+
        +-+
seed 4 -+ |
          +- final
seed 2 -+ |
        +-+
seed 3 -+
```

The club draws every sheet by two rules:

* Suppose the better seed wins every match it plays.
Then in every round, the first round included, the best player still in the draw must meet the worst player still in the draw, the second-best must meet the second-worst, and so on.
* The better seed is always written higher: of the two names in a first-round match, the better seed comes first; of two first-round matches whose winners meet, the match holding the better seed comes first; and the same for two groups of four names, of eight, and so on whose winners meet.

Return the sheet as a list of names from top to bottom.
A single entrant wins without playing, and the sheet is just that one name.

Constraints: `1 <= n <= 32`, where `n` is the number of entrants in `players`, and `n` is a power of two.
Names are distinct and non-empty.
"""
import unittest

def drawSheet(players):
    """Return the sheet, top to bottom, as a list of names."""
    # Linked list, implemented as a dict where each key points to the next key.
    linked_list = {1: None}
    # Start with the winner, then repeatedly double the number of players,
    # inserting them into the linked list.
    # 1 -> 1-2 -> 1-4; 2-3 -> 1-8; 4-5; 2-7; 3-6
    # Each round we add the bottom half, eg [5..8], inserting them after their competitor.
    while len(linked_list) < len(players):
        prior_len = len(linked_list)
        for p in range(prior_len):
            wins = p + 1
            loses = prior_len * 2 - p
            prior = linked_list[wins]

            linked_list[wins] = loses
            linked_list[loses] = prior

    # Walk the "sheet"/linked list, mapping player numbers to names.
    out = []
    cur = 1
    while cur in linked_list:
        out.append(players[cur - 1])
        cur = linked_list[cur]
    return out


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(drawSheet(["Ada", "Bram", "Cleo", "Dev", "Esme", "Farid", "Gwen", "Hugo"]), ["Ada", "Hugo", "Dev", "Esme", "Bram", "Gwen", "Cleo", "Farid"])
        self.assertEqual(drawSheet(["Ada", "Bram", "Cleo", "Dev"]), ["Ada", "Dev", "Bram", "Cleo"])
        self.assertEqual(drawSheet(["Ada", "Bram"]), ["Ada", "Bram"])

if __name__ == "__main__":
    unittest.main()
