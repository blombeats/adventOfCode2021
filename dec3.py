import numpy as np


with open("dec3_input.txt", "r") as f:
    data = f.readlines()
data=[x[:-1] for x in data]  # remove endline (there's a better way to do this, but I'm lazy)

data=np.array([[int(y) for y in x] for x in data]) #convert text to list of ints

print(f"Data length: {len(data)}")


d=data[:10] #for testing

first_col=data[:]

newBits=[]
#Iterate over a columns in the data
for i in range(data.shape[1]):
    newBits.append(
        np.unique(data[:,i],return_counts=True)
    )

gammaRate=[x[1].argmax() for x in newBits]
epsilonRate=[x[1].argmin() for x in newBits]


#Convert to decimal int
gammaRateDecimal=int("".join([str(x) for x in gammaRate]),2)
epsilonRateDecimal=int("".join([str(x) for x in epsilonRate]),2)
powerConsumption=gammaRateDecimal*epsilonRateDecimal

print(f"Power Consumption: {powerConsumption}")





#data=[int(x,2) for x in data] #convert to decimal ints