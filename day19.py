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


class Scanner:
    """
    Data contains the beacons


    """

    def __repr__(self):
        return str(self.data)

    def __init__(self, data, id=0, x=None, y=None, z=None):

        self.detectionRange = 1000  # units in all axis (x,y,z)
        # detection relative to the scanner
        # scanners cannot detect other scanners

        self.id = id

        if id == 0:
            self.posAbs = np.array([0, 0, 0], dtype=int)
        elif x:
            self.posAbs = np.array([x, y, z], dtype=int)
        else:
            self.posAbs = np.array([np.nan] * 3)  # scanner0 is at 0,0,0

        self.offsetX = 0
        self.offsetY = 0

        self.rot = np.array([1] * 3)  # 90 degree clicks in all directions. 24 different orientations
        self.view = None  # Vad denna scanner ser
        self.data = data  # relative position
        self.dataAbs = np.zeros_like(data)  # absolute position

        self._createView()

        self.render()

    def detectPattern(self):
        pass

    def _createView(self):
        # 0,0 is bottom left
        maxX = np.max(self.data[:, 0]) + 1
        maxY = np.max(self.data[:, 1]) + 1

        self.view = np.zeros([maxY, maxX], dtype=int)

    def render(self):
        for x, y in self.data:
            self.view[-abs(y) - 1, x] = 1

        print(self.view)

    def resetView(self):
        # reset
        self.view[:, :] = 0


# data = loadData('dec19_input.txt')
data = loadData('dec19_test2.txt')
data = splitData(data)

# scanners
s = [Scanner(x, id=i) for i, x in enumerate(data)]

self = s[1]

# print(s[0].beacons)

# The submarine has automatically summarized the relative positions
# of beacons detected by each scanner (your puzzle input).


# find pairs of scanners
