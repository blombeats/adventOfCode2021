import numpy as np


def loadData(filename):
    with open(filename, "r") as f:
        data = f.readlines()

    data = [x.replace("\n", "") for x in data]

    return data


data = loadData('dec5_test.txt')
data = loadData('dec5_input.txt')

data = np.array([[[int(z) for z in y.split(",")] for y in x.split(" -> ")] for x in data])

len(data)
# x1,y1 x2,y2


# filter to only horizontal and vertical lines
cords = np.array([x for x in data if x[0][0] == x[1][0] or x[0][1] == x[1][1]])

print(f"data: {len(data)}")
print(f"cords: {len(cords)}")

# get max x y cordinates
cordsMax = np.max(cords)
print(f"CordsMax: {cordsMax}")

# create map (zeros)
myMap = np.zeros([cordsMax + 1, cordsMax + 1])
print(f"mymap shape {myMap.shape}")

# convert to int
data = data.astype(int)


IF Horizon or or VERTIAL OR DIAGONAL
# draw lines
for x in cords:

    # The smallest value in the right place
    if x[0][0] < x[1][0]:
        x1 = x[0][0]
        x2 = x[1][0]
    else:
        x1 = x[1][0]
        x2 = x[0][0]

    if x[0][1] < x[1][1]:
        y1 = x[0][1]
        y2 = x[1][1]
    else:
        y1 = x[1][1]
        y2 = x[0][1]

    myMap[y1:y2 + 1, x1:x2 + 1] += 1

x = data[1]

# Diagonal
for x in data:
    # Detta är felet! De swappar valörer mellan arrerna.
    # TODO
    # lös detta de ska inte kunna flytta 0 till 1 i andra arrayen osv

    X = x[:, 0]
    Y = x[:, 1]

    # is it diagonal
    if X[0] > X[1]:
        xDiff = X[0] - X[1]
    elif X[0] < X[1]:
        xDiff = X[1] - X[0]
    elif X[0] == X[1]:
        xDiff = 0
    else:
        ValueError(f"X - x: {X} y: {Y}")

    if Y[0] > Y[1]:
        yDiff = Y[0] - Y[1]
    elif Y[0] < Y[1]:
        yDiff = Y[1] - Y[0]
    elif Y[0] == Y[1]:
        yDiff = 0
    else:
        ValueError(f"Y - x: {X} y: {Y}")

    if xDiff == yDiff:
        # its diagonal

        xAxis = range(X[0], X[1] + 1, 1) if X.argmin() == 0 else range(X[0], X[1] - 1, -1)
        yAxis = range(Y[0], Y[1] + 1, 1) if Y.argmin() == 0 else range(Y[0], Y[1] - 1, -1)

        nummer = list(zip(xAxis, yAxis))

        if not len(xAxis) == len(yAxis) == len(nummer):
            raise ValueError

        for a, b in nummer:
            myMap[a, b] += 1

result = (myMap >= 2).sum()

print(myMap)

print(f"Result: {result}")
