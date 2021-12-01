import numpy as np



with open("dec1_input.txt", "r") as f:
    data = f.readlines()

data = [int(x[:-1]) for x in data if x]  # remove endline (there's a better way to do this, but I'm lazy)

print(f"Data length: {len(data)}")

"""
data = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    280
]

"""

# data=data[:7]
timesLarger = 0
for i in range(len(data) - 1):
    if data[i + 1] > data[i]:
        #print("more")
        timesLarger += 1

print(timesLarger) #Svaret
# Lösning #1


#################### Lösning 2


def rolling_window(a: np.ndarray, window):
    shape = a.shape[:-1] + (a.shape[-1] - window + 1, window)
    strides = a.strides + (a.strides[-1],)
    return np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)



#data=np.array(data[:10]) #Test
data=np.array(data)
data=rolling_window(data,3)
data=[np.sum(x) for x in data]


timesLarger = 0
for i in range(len(data) - 1):
    if data[i + 1] > data[i]:
        #print("more")
        timesLarger += 1

print(timesLarger)
# Lösning #1








# Lösning 2
