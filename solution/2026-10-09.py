"""Where Two Cuttings Meet

A field botanist keeps a ledger of wild specimens, each grown from one earlier specimen except for a single founder.

Specimen names are listed in `specimenNames`.
The ledger is `lineage`, and `lineage[i]` is the index of the specimen that specimen i was grown from, or -1 when i is the founder.
Exactly one specimen is the founder, and following `lineage` from any specimen reaches that founder.
Given indices `firstIndex` and `secondIndex`, which may name the same specimen, walk from each index back to the founder.
Each walk includes its starting specimen.
Return the name of the specimen that lies on both walks and sits farthest from the founder.

### Constraints

* `lineage` and `specimenNames` each hold n entries, and n is an integer from 1 to 20
* every value in `lineage` is -1 or an index from 0 to n - 1
* `firstIndex` and `secondIndex` are each an index from 0 to n - 1
"""
import unittest

def sharedSpecimenName(lineage, specimenNames, firstIndex, secondIndex):
    """Return the name of the item farthest from the root on both walks."""
    seen = set()
    while firstIndex != -1:
        seen.add(firstIndex)
        firstIndex = lineage [firstIndex]
    while secondIndex not in seen:
        secondIndex = lineage[secondIndex]
    return specimenNames[secondIndex]


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(sharedSpecimenName([-1, 0, 0], ["oak", "ash", "elm"], 1, 2), "oak")
        self.assertEqual(sharedSpecimenName([-1, 0, 1], ["oak", "ash", "elm"], 1, 2), "ash")
        self.assertEqual(sharedSpecimenName([-1, 0], ["oak", "ash"], 1, 1), "ash")
        self.assertEqual(sharedSpecimenName([1, -1, 1], ["ash", "oak", "elm"], 0, 2), "oak")
        self.assertEqual(sharedSpecimenName([-1, 0, 1, 2, 1], ["root", "mid", "low", "deep", "side"], 3, 4), "mid")
        self.assertEqual(sharedSpecimenName([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], ["n0", "n1", "n2", "n3", "n4", "n5", "n6", "n7", "n8", "n9", "n10", "n11", "n12", "n13", "n14", "n15", "n16", "n17", "n18", "n19"], 19, 7), "n7")

if __name__ == "__main__":
    unittest.main()
