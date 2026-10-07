"""The Understudy's Ledger

A stage manager keeps a ledger of every understudy's cue calls, each call written as a string of lowercase letters.
Two calls follow the same shape when one can be turned into the other by swapping each letter for a single stand-in letter, the same letter always getting the same stand-in and no two letters sharing one.
Given a reference call `reference` and a list of candidate calls `candidates`, all the same length as the reference, return the candidates that follow the reference's shape, in the order they are given.
Return an empty list when none of them do.

### Constraints

* 1 <= reference length <= 8
* 0 <= candidate count <= 6
* all strings are made of lowercase letters
"""
import unittest
import collections

def normalize(name: str) -> list[int]:
    seen = {}
    out = []
    for i in name:
        if i not in seen:
            seen[i] = len(seen)
        out.append(seen[i])
    return out


def matchingPatterns(reference, candidates):
    """Return the candidates whose pattern of repeats matches the reference."""
    target = normalize(reference)
    return [i for i in candidates if normalize(i) == target]


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(matchingPatterns("abab", ["cdcd", "cdee", "abcd", "efef"]), ["cdcd", "efef"])
        self.assertEqual(matchingPatterns("abc", ["pqp", "xyz", "xxy"]), ["xyz"])
        self.assertEqual(matchingPatterns("aab", ["bba", "abc", "ccb"]), ["bba", "ccb"])
        self.assertEqual(matchingPatterns("abab", ["abca", "cdcd"]), ["cdcd"])
        self.assertEqual(matchingPatterns("abb", ["baa", "bab", "abc", "aba"]), ["baa"])
        self.assertEqual(matchingPatterns("abcdabcd", ["wxyzwxyz", "aaaaaaaa", "abcdefgh", "pqrspqrs", "aabbccdd", "xyxyxyxy"]), ["wxyzwxyz", "pqrspqrs"])

if __name__ == "__main__":
    unittest.main()
