from time import sleep

import numpy as np


def loadData():
    with open("dec3_input.txt", "r") as f:
        data = f.readlines()
    data = [x[:-1] for x in data]  # remove endline (there's a better way to do this, but I'm lazy)

    data = np.array([[int(y) for y in x] for x in data])  # convert text to list of ints

    print(f"Data length: {len(data)}")
    return data


def convertNpDecimal(arr: np.ndarray):
    return int("".join([str(x) for x in arr]), 2)


def doTheStuff(data, common="most"):
    i = 0
    while len(data) > 1:
        counts = np.unique(data[:, i], return_counts=True)

        if len(counts[1]) == 2:
            if counts[1][0] == counts[1][1]:
                if common == "most":
                    mostCommon = 1
                elif common == "least":
                    mostCommon = 0
            else:
                if common == "most":
                    mostCommon = counts[1].argmax()
                elif common == "least":
                    mostCommon = counts[1].argmin()
        elif len(counts[1]) == 1:
            if common == "most":
                mostCommon = counts[0][0]  # TODO Might not work
            elif common == "least":
                mostCommon = counts[0][0]  # TODO Might not work
        else:
            ValueError("NONONO")

        filt = data[:, i].astype(bool)  # create filter based if mostCommon is 1

        # noinspection PyUnboundLocalVariable
        if mostCommon == 0:
            filt = np.invert(filt)

        # Filter data
        data = data[filt, :]  # filtered view
        i += 1

    print("DONE!")

    print(f"Data length: {len(data)}")

    if len(data) == 1:
        data = data[0]
    else:
        ValueError("NOooooo1")

    return data


# data = data[:5]  # for testing
data = loadData()

oxygenGeneratorRating = doTheStuff(data, common="most")
Co2ScrubberRating = doTheStuff(data, common="least")

oxygenGeneratorRating = convertNpDecimal(oxygenGeneratorRating)
Co2ScrubberRating = convertNpDecimal(Co2ScrubberRating)


lifeSupportRating = oxygenGeneratorRating * Co2ScrubberRating

print(f"lifeSupportRating: {lifeSupportRating}")
