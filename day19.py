import numpy as np


def loadData(filename):
    with open(filename, "r") as f:
        data = f.readlines()

    data = [x.replace("\n", "") for x in data]

    return data


def splitData(data):
    stuff = []
    for i in range(len(data)):
        if "---" in data[i]:
            stuff.append({'i': i})

    print(stuff)

    datasplit = []

    for i in range(len(stuff) - 1):
        datasplit.append(
            data[stuff[i]['i']:stuff[i + 1]['i']]
        )

    print(datasplit[0])

    # remove empty

    datasplit = [[[int(z) for z in y.split(",")] for y in x if not "---" in y and y] for x in datasplit]

    datasplit = [np.array(x, dtype=int) for x in datasplit]

    datasplit = np.array(datasplit)

    return datasplit


class beacon:
    def __init__(self):
        self.pos = np.array([np.nan] * 3)
        pass


class scanner:
    def __init__(self):
        self.detectionRange = 1000  # units in all axis (x,y,z)
        # detection relative to the scanner
        # scanners cannot detect other scanners

        self.pos = np.array([np.nan] * 3)
        self.rot = np.array([np.nan] * 3)  # 90 degree clicks in all directions. 24 different orientations

        self.detectedBeacons = []

        # You'll need to determine the positions of the beacons and scanners yourself.

    def dectection(self):
        pass
        # For example,
        # if a scanner is at x, y, z coordinates 500, 0, -500
        # and there are beacons at -500, 1000, -1500 and 1501, 0, -500,
        # the scanner could report that the first beacon is at -1000, 1000, -1000
        # (relative to the scanner) but would not detect the second beacon at all.

    def overlappingRegion(self, otherScanner):
        # at least 12 beacons
        pass


class Overlapping:
    def __init__(self, scanners: list):
        self.scanners = scanners
        self.overlappingBeacons = 0

        pass


data = loadData('dec19_test.txt')
data=splitData(data)

# The submarine has automatically summarized the relative positions
# of beacons detected by each scanner (your puzzle input).


# find pairs of scanners
