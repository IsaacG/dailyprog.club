"""Festival Banners

At a harvest festival, each stall keeps its apple count in the array baskets.
To help visitors compare, every stall hangs a banner showing the product of the apple counts of every other stall.

Return an array where result[i] is the number shown on stall i's banner.

Constraints:

* 1 <= n <= 10, where n is the length of baskets
* Each count is an integer from 0 to 9
* The product of an empty set of counts is 1
"""

import math

def otherProducts(baskets):
    # result[i] = product of all counts except baskets[i]
    zeroes = baskets.count(0)
    if zeroes >= 2:
        return [0] * len(baskets)
    if zeroes == 1:
        result = [0] * len(baskets)
        result[baskets.index(0)] = math.prod(i for i in baskets if i != 0)
        return result
    prod = math.prod(baskets)
    return [prod // i for i in baskets]

assert otherProducts([2, 3, 4]) == [12, 8, 6]
assert otherProducts([1, 5]) == [5, 1]
assert otherProducts([2, 3, 4, 5, 6, 7, 8, 9, 1, 2]) == [362880, 241920, 181440, 145152, 120960, 103680, 90720, 80640, 725760, 362880]
