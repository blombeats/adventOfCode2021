import numpy as np

def convertNpDecimal(arr: np.ndarray):
    return int("".join([str(x) for x in arr]), 2)


def loadData():
    with open('dec4_input.txt', "r") as f:
        data = f.readlines()

    data = [x[:-1] for x in data]  # remove endline (there's a better way to do this, but I'm lazy)

    drawOrder=data.pop(0)
    drawOrder=drawOrder.split(",")
    drawOrder=[int(x) for x in drawOrder]


    boards=[]

    for i in range(0,len(data),6):
        newBoard=np.zeros([5,5],dtype=int)

        for y in range(1,6): #Skip first one as it's empty
            newBoard[y]=data[i+y].split()

        boards.append(newBoard)

    return drawOrder,boards

drawOrder,boards=loadData()
