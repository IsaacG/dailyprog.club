"""Cross-Country Drive

You're planning a cross-country drive.
Your car starts with a full tank of `startFuel` liters.
Along the way, there are `stations`: each is a pair `[distance, fuel]` where `distance` is the distance from the start (in miles) and `fuel` is the amount of fuel the station offers (positive integers).
You can stop at any station to refuel, adding its full fuel to your tank.
You need to reach your destination `target` miles away.
What is the minimum number of refueling stops needed to reach `target`? If impossible, return `-1`.
Stations are not necessarily sorted by distance.
"""
import unittest

def minStops(target, startFuel, stations):
    """Return minimum number of refueling stops, or -1 if impossible."""
    total_fuel = startFuel
    stops = 0
    stations.sort(key=lambda x: (-x[1], x[0]))
    while total_fuel < target:
        stop = next(
            (idx for idx, (distance, fuel) in enumerate(stations) if distance <= total_fuel),
            None,
        )
        if stop is None:
            return -1
        distance, fuel = stations.pop(stop)
        total_fuel += fuel
        stops += 1
    return stops


class TestSolution(unittest.TestCase):
    def test_data(self):
        self.assertEqual(minStops(100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]]), 2)
        self.assertEqual(minStops(1, 1, []), 0)
        self.assertEqual(minStops(100, 1, [[10, 100]]), -1)
        self.assertEqual(minStops(10, 5, [[5, 5]]), 1)
        self.assertEqual(minStops(10, 5, []), -1)
        self.assertEqual(minStops(100, 10, [[10, 10], [20, 10], [30, 10], [40, 10], [50, 10], [60, 10], [70, 10], [80, 10], [90, 10]]), 9)
        self.assertEqual(minStops(500, 50, [[10, 5], [20, 5], [30, 5], [40, 5], [50, 5], [60, 5], [70, 5], [80, 5], [90, 5], [100, 5], [110, 5], [120, 5], [130, 5], [140, 5], [150, 5], [160, 5], [170, 5], [180, 5], [190, 5], [200, 5], [210, 5], [220, 5], [230, 5], [240, 5], [250, 5], [260, 5], [270, 5], [280, 5], [290, 5], [300, 5]]), -1)

if __name__ == "__main__":
    unittest.main()
