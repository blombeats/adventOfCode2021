import numpy as np


def loadData(filename):
    with open(filename, "r") as f:
        data = f.readlines()

    data = [x.replace("\n", "") for x in data]

    return data


def splitData(data):
    ranges = []
    for i in range(len(data)):
        if "---" in data[i]:
            ranges.append(i)

    print(ranges)

    datasplit = []

    for i in range(len(ranges)):
        if i == len(ranges) - 1:
            datasplit.append(data[ranges[i]:])
        else:
            datasplit.append(data[ranges[i]:ranges[i + 1]])
    print(datasplit)

    # remove empty

    datasplit = [[[int(z) for z in y.split(",")] for y in x if not "---" in y and y] for x in datasplit]

    datasplit = [np.array(x, dtype=int) for x in datasplit]

    datasplit = np.array(datasplit)

    return datasplit


class Beacon:
    def __init__(self, x=None, y=None, z=None):

        self.posAbs = np.array([np.nan] * 3)
        if x or y or z:
            self.posRel = np.array([x, y, z], dtype=int)  # relative
        else:
            raise ValueError(f"X:{x}, Y:{y}, Z:{z}")
            # self.posRel = np.array([np.nan] * 3)  # relative

    def __repr__(self):
        return f"Beacon | Rel:{self.posRel} Abs:{self.posAbs} "


class Scanner:
    def __repr__(self):
        return str(self.data)

    def __init__(self, data, id=0, x=None, y=None, z=None):
        self.detectionRange = 1000  # units in all axis (x,y,z)
        # detection relative to the scanner
        # scanners cannot detect other scanners

        self.id = id

        if x:
            self.posAbs = np.array([x, y, z], dtype=int)
        else:
            self.posAbs = np.array([np.nan] * 3)  # scanner0 is at 0,0,0

        self.rot = np.array([1] * 3)  # 90 degree clicks in all directions. 24 different orientations
        self.view = None  # Vad denna scanner ser
        self.beacons = []
        self.data = data

        self.createBeacons()

        # You'll need to determine the positions of the beacons and scanners yourself.

    def createBeacons(self):
        for b in self.data:
            self.beacons.append(Beacon(x=b[0], y=b[1], z=0))

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


# data = loadData('dec19_input.txt')
data = loadData('dec19_test2.txt')
data = splitData(data)

# scanners
s = [Scanner(x,id=i) for i, x in enumerate(data)]

print(s[0].beacons)

# The submarine has automatically summarized the relative positions
# of beacons detected by each scanner (your puzzle input).


# find pairs of scanners
