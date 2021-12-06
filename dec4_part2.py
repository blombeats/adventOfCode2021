import numpy as np


def convertNpDecimal(arr: np.ndarray):
    return int("".join([str(x) for x in arr]), 2)


def loadData():
    with open('dec4_input.txt', "r") as f:
        data = f.readlines()

    data = [x.replace("\n","") for x in data]  # remove endline (there's a better way to do this, but I'm lazy)

    drawOrder = data.pop(0)
    drawOrder = drawOrder.split(",")
    drawOrder = np.array([int(x) for x in drawOrder])

    boards = []

    for i in range(0, len(data), 6):

        currentBoard = data[i:i + 6]
        currentBoard = [[int(y) for y in x.split()] for x in currentBoard if x]

        newBoard = np.zeros([5, 5], dtype=int)

        for y in range(len(currentBoard)):  # Skip first one as it's empty
            newBoard[y] = currentBoard[y]

        boards.append(newBoard)

    return drawOrder, np.array(boards)


def checkBingo(stats):
    bingo = False

    # Check rows
    for i in range(len(stats)):
        if stats[i].all() == True:
            bingo = True
            break

    # Columns
    for i in range(len(stats)):
        if stats[:, i].all() == True:
            bingo = True
            break

    return bingo


def calcBoard(board, drawOrder):
    """

    :param board:
    :param drawOrder:
    :return: number of draws it took to win and if won att all
    """

    bingo = False

    stats = np.zeros([5, 5], dtype=bool)
    """
        Show 1 if its been drawn at that location
        Show 0 if not drawn
    """
    draw = 0  # IDE complained on me

    for draw in range(len(drawOrder)):
        # print(draw)

        stats += board == drawOrder[draw]  # adds all true to the stats

        bingo = checkBingo(stats)
        if bingo:
            break
    if bingo:

        return np.array([draw, board, stats,drawOrder[draw]])
    else:
        return False


def playGames(boards, drawOrder):
    # Play all games
    games = []
    for b in boards:
        games.append(calcBoard(b, drawOrder))

    # Filter games
    games = [x for x in games if x is not False]
    print(f"Won Games: {len(games)}")

    bestGame = max([x[0] for x in games])

    bestGames = [x for x in games if x[0] == bestGame]

    if len(bestGames) > 1:
        raise ValueError("nono seniior")

    return bestGames[0]


def calcPoints(game):
    unmarkedSum = game[1][np.invert(game[2])].sum()
    lastCalled = game[3]
    return unmarkedSum * lastCalled


drawOrder, boards = loadData()

lastGame = playGames(boards, drawOrder) #Best game

score=calcPoints(lastGame)

print(f"Score: {score}")