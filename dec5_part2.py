import numpy as np


def loadData(filename):
    with open(filename, "r") as f:
        data = f.readlines()

    data = [x.replace("\n", "") for x in data]

    return data


def createMap(data):
    # get max x y cordinates
    cordsMax = np.max(data)
    print(f"CordsMax: {cordsMax}")

    # create map (zeros)
    myMap = np.zeros([cordsMax + 1, cordsMax + 1])
    print(f"mymap shape {myMap.shape}")
    return myMap


def drawLinesHV(x, myMap):
    # The smallest value in the right place
    # X
    if x[0][0] < x[1][0]:
        x1 = x[0][0]
        x2 = x[1][0]
    else:
        x1 = x[1][0]
        x2 = x[0][0]

    # Y
    if x[0][1] < x[1][1]:
        y1 = x[0][1]
        y2 = x[1][1]
    else:
        y1 = x[1][1]
        y2 = x[0][1]

    myMap[y1:y2 + 1, x1:x2 + 1] += 1
    return myMap


def isDiagonal(x):
    X = x[:, 0]
    Y = x[:, 1]

    # is it diagonal
    if X[0] > X[1]:
        xDiff = X[0] - X[1]
    elif X[0] < X[1]:
        xDiff = X[1] - X[0]
    elif X[0] == X[1]:
        return False

    if Y[0] > Y[1]:
        yDiff = Y[0] - Y[1]
    elif Y[0] < Y[1]:
        yDiff = Y[1] - Y[0]
    elif Y[0] == Y[1]:
        return False

    if xDiff == yDiff:
        # its diagonal
        return True
    else:
        return False


def drawLinesDiagonal(x, myMap):
    X = x[:, 0]
    Y = x[:, 1]

    xAxis = range(X[0], X[1] + 1, 1) if X.argmin() == 0 else range(X[0], X[1] - 1, -1)
    yAxis = range(Y[0], Y[1] + 1, 1) if Y.argmin() == 0 else range(Y[0], Y[1] - 1, -1)

    nummer = list(zip(xAxis, yAxis))

    if not len(xAxis) == len(yAxis) == len(nummer):
        raise ValueError

    for a, b in nummer:
        myMap[b,a] += 1
    return myMap

data = loadData('dec5_test.txt')
data = loadData('dec5_input.txt')

data = np.array([[[int(z) for z in y.split(",")] for y in x.split(" -> ")] for x in data])

myMap = createMap(data)

for d in data:
    if isDiagonal(d):
        # Diagonal
        print(f"{d} | Diagonal")
        myMap = drawLinesDiagonal(d, myMap)
    elif d[0][1] == d[1][1]:
        # Horizontal
        print(f"{d} | Horizontal")
        myMap = drawLinesHV(d, myMap)
    elif d[0][0] == d[1][0]:
        # Vertical
        print(f"{d} | Vertical")
        myMap = drawLinesHV(d, myMap)

    else:# isDiagonal(d):
        raise ValueError("NOO")


print(myMap)

result = (myMap >= 2).sum()
print(f"Result: {result}")
