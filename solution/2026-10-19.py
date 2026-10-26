"""The Stamp Dealer's Run

A stamp dealer keeps her stock in labelled boxes, each box holding several identical stamps of one printed value, and a customer wants to build every postage total from 1 upward without gaps.

You are given `values`, where `values[i]` is the printed value of the stamps in box i, and `counts`, where `counts[i]` is how many stamps that box holds.
A set of stamps may take at most `counts[i]` stamps from box i, and its total is the sum of the printed values taken.
Return the largest integer L such that every whole number from 1 to L can be made as the total of some set of stamps.
Return 0 if 1 cannot be made at all.

### Constraints

* 1 <= number of boxes <= 200
* 1 <= number of copy counts <= 200, matching the number of boxes
* every printed value is an integer from 1 to 100000 inclusive
* every copy count is an integer from 1 to 100 inclusive
"""
import unittest
import collections
import itertools

def minus(stamps, remove):
    stamps = stamps.copy()
    if stamps[remove] == 1:
        del stamps[remove]
    else:
        stamps[remove] -= 1
    return stamps

def largestCoverage(values, counts):
    # return the largest L such that every amount from 1 to L can be formed
    largest = 0
    for val, count in sorted(zip(values, counts)):
        if val > largest + 1:
            break
        largest += val * count
    return largest

    stamps = collections.defaultdict(int)
    for val, count in zip(values, counts):
        stamps[val] += count
    values = [i for i, j in sorted(stamps.items(), reverse=True)]
    counts = tuple(j for i, j in sorted(stamps.items(), reverse=True))

    idx = {v: i for i, v in enumerate(values)}

    def minus(counts, remove):
        i = idx[remove]
        return counts[:i] + (counts[i] - 1,) + counts[i + 1:]

    covers = {}
    for val in values:
        covers[val] = minus(counts, val)

    for target in itertools.count(1):
        if target in covers:
            continue
        for v, i in idx.items():
            if target > v and (r := covers[target - v])[i]:
                covers[target] = minus(r, v)
                break
        else:
            return target - 1


    singles = [
        {value * i for i in range(1, count + 1)} for value, count in zip(values, counts)
    ]
    covers = set()
    n = 0
    for target in itertools.count(1):
        if target and not target % 100:
            print(target, len(covers), n)
        while target not in covers and n <= len(singles):
            n += 1
            for combo in itertools.combinations(singles, n):
                for prod in itertools.product(*combo):
                    covers.add(sum(prod))
        if target not in covers:
            return target - 1
                


    stamps = sorted(zip(values, counts), reverse=True)
    
    def can_cover(target):
        for val, avail in stamps:
            num = min(avail, target // val)
            target -= val * num
        return target == 0

    for target in itertools.count(1):
        if can_cover(target):
            continue
        return target - 1

    stamps = []
    for value, count in zip(values, counts):
        stamps.extend([value] * count)
    combos = {sum(i) for num in range(1, len(stamps) + 1) for i in itertools.combinations(stamps, num)}
    return next(i for i in itertools.count(1) if i not in combos) - 1


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(largestCoverage([1, 2, 5], [2, 1, 1]), 9)
        self.assertEqual(largestCoverage([1, 3], [1, 1]), 1)
        self.assertEqual(largestCoverage([1, 2], [1, 1]), 3)
        self.assertEqual(largestCoverage([5, 1, 2], [1, 2, 1]), 9)
        self.assertEqual(largestCoverage([1], [5]), 5)
        self.assertEqual(largestCoverage([2, 3], [1, 1]), 0)
        self.assertEqual(largestCoverage([2, 1, 2], [1, 3, 1]), 7)
        # self.assertEqual(largestCoverage([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200], [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]), 2010000)

if __name__ == "__main__":
    unittest.main()
