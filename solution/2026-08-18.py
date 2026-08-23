"""The Lakeside Roster

The lake trail has `n` observation blinds in a row, and `sightings` is an array with `n` entries: `sightings[i]` is the number of sightings logged at blind i.

The park assigns exactly `k` rangers to the trail.
Each ranger watches one contiguous block of blinds, every blind is watched by exactly one ranger, and every block is non-empty.
The busiest ranger's block total sets the pace for the day.

Return the smallest possible value for that largest block total.

### Constraints

* 2 <= `n` <= 250, where `n` is the length of `sightings`
* 1 <= `k` <= `n`
* 0 <= `sightings[i]` <= 1,000,000
"""
import unittest
import functools

def lookoutRoster(times, climbers):  # 2026/08/08
    """Return the smallest possible heaviest patrol total."""
    # Matches 2026-08-08

    @functools.cache
    def best(acc, idx, climbers):
        if climbers == 1:
            return sum(times[idx:])
        if idx + climbers == len(times):
            b = max(times[-(climbers - 1):])
            return max(b, acc + times[idx])
        return min(
            max(acc + times[idx], best(0, idx + 1, climbers - 1)),
            best(acc + times[idx], idx + 1, climbers)
        )

    return best(0, 0, climbers)


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(lookoutRoster([3, 2, 4, 1, 5], 2), 9)
        self.assertEqual(lookoutRoster([7, 2, 8, 3], 4), 8)
        self.assertEqual(lookoutRoster([10, 20, 30, 40, 50, 60], 3), 90)
        self.assertEqual(lookoutRoster([1, 9, 2, 8], 2), 10)
        self.assertEqual(lookoutRoster([5, 5], 1), 10)
        self.assertEqual(lookoutRoster([5, 5], 2), 5)
        self.assertEqual(lookoutRoster([0, 0, 0], 3), 0)
        self.assertEqual(lookoutRoster([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40], 20), 57)
        self.assertEqual(lookoutRoster([4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 15), 16)
        self.assertEqual(lookoutRoster([1000000, 1, 1, 1, 1, 1], 2), 1000000)
        self.assertEqual(lookoutRoster([3, 8, 13, 18, 23, 28, 33, 38, 43, 48, 53, 58, 63, 68, 73, 78, 83, 88, 93, 98, 103, 108, 113, 118, 123, 128, 133, 138, 143, 148, 153, 158, 163, 168, 173, 178, 183, 188, 193, 198, 203, 208, 213, 218, 223, 228, 233, 238, 243, 248, 253, 258, 263, 268, 273, 278, 283, 288, 293, 298, 303, 308, 313, 318, 323, 328, 333, 338, 343, 348, 353, 358, 363, 368, 373, 378, 383, 388, 393, 398, 403, 408, 413, 418, 423, 428, 433, 438, 443, 448, 453, 458, 463, 468, 473, 478, 483, 488, 493, 498, 503, 508, 513, 518, 523, 528, 533, 538, 543, 548, 553, 558, 563, 568, 573, 578, 583, 588, 593, 598, 603, 608, 613, 618, 623, 628, 633, 638, 643, 648, 653, 658, 663, 668, 673, 678, 683, 688, 693, 698, 703, 708, 713, 718, 723, 728, 733, 738, 743, 748, 753, 758, 763, 768, 773, 778, 783, 788, 793, 798, 803, 808, 813, 818, 823, 828, 833, 838, 843, 848, 853, 858, 863, 868, 873, 878, 883, 888, 893, 898, 903, 908, 913, 918, 923, 928, 933, 938, 943, 948, 953, 958, 963, 968, 973, 978, 983, 988, 993, 998, 1003, 1008, 1013, 1018, 1023, 1028, 1033, 1038, 1043, 1048, 1053, 1058, 1063, 1068, 1073, 1078, 1083, 1088, 1093, 1098, 1103, 1108, 1113, 1118, 1123, 1128, 1133, 1138, 1143, 1148, 1153, 1158, 1163, 1168, 1173, 1178, 1183, 1188, 1193, 1198, 1203, 1208, 1213, 1218, 1223, 1228, 1233, 1238, 1243, 1248], 12), 13453)

if __name__ == "__main__":
    unittest.main()
