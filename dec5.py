import numpy as np

def loadData():
    with open('dec4_input.txt', "r") as f:
        data = f.readlines()

    data = [x.replace("\n","") for x in data]  # remove endline (there's a better way to do this, but I'm lazy)

    return data

def processData(data):


data=loadData()


drawOrder = np.array([int(x) for x in data])

    boards = []

    for i in range(0, len(data), 6):

        currentBoard = data[i:i + 6]
        currentBoard = [[int(y) for y in x.split()] for x in currentBoard if x]

        newBoard = np.zeros([5, 5], dtype=int)

        for y in range(len(currentBoard)):  # Skip first one as it's empty
            newBoard[y] = currentBoard[y]

        boards.append(newBoard)