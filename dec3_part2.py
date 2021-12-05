from time import sleep

import numpy as np

with open("dec3_input.txt", "r") as f:
    data = f.readlines()
data = [x[:-1] for x in data]  # remove endline (there's a better way to do this, but I'm lazy)

data = np.array([[int(y) for y in x] for x in data])  # convert text to list of ints

print(f"Data length: {len(data)}")

d = data[:5]  # for testing



for i in range(len(d)): #TODO replace with data
    print(d[i])
    mostCommon=np.unique(d[i],return_counts=True)[1].argmax()
    #print(mostCommon)

    #filter out
    for y in range(len(d[i])):
        if d[i][y]!=mostCommon:
            print(f"nono: {d[i][y]}")
            column=y
            d=np.delete(d,column,1)
        #print(d[:,y])


newBits = []
# Iterate over a columns in the data
for i in range(data.shape[1]):
    newBits.append(
        np.unique(data[:, i], return_counts=True)
    )

gammaRate = [x[1].argmax() for x in newBits]
epsilonRate = [x[1].argmin() for x in newBits]

# Convert to decimal int
gammaRateDecimal = int("".join([str(x) for x in gammaRate]), 2)
epsilonRateDecimal = int("".join([str(x) for x in epsilonRate]), 2)
powerConsumption = gammaRateDecimal * epsilonRateDecimal

print(f"Power Consumption: {powerConsumption}")


















oxygenGeneratorRating = None
COScrubberRating = None
lifeSupportRating = oxygenGeneratorRating * COScrubberRating

print(f"lifeSupportRating: {lifeSupportRating}")
