import numpy as np

def loadData(filename):
    with open(filename, "r") as f:
        data = f.readlines()

    data = [x.replace("\n", "") for x in data]

    return data


class scanner:
    def __init__(self):
        self.detectionRange = 1000  # units in all axis (x,y,z)
        # detection relative to the scanner
        # scanners cannot detect other scanners

        self.position = np.array([np.nan] * 3)

        #You'll need to determine the positions of the beacons and scanners yourself.

    def dectection(self):
        pass
        # For example,
        # if a scanner is at x, y, z coordinates 500, 0, -500
        # and there are beacons at -500, 1000, -1500 and 1501, 0, -500,
        # the scanner could report that the first beacon is at -1000, 1000, -1000
        # (relative to the scanner) but would not detect the second beacon at all.


class beacon:
    def __init__(self):
        self.position=np.array([np.nan]*3)
        pass

# The submarine has automatically summarized the relative positions
# of beacons detected by each scanner (your puzzle input).
