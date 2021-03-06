import numpy as np

def loadData(filename):
    with open(filename,"r") as f:
        data=f.readlines()

    data=[x.replace("\n","") for x in data]

    return data


data=loadData('dec5_test.txt')
data=loadData('dec5_input.txt')

data=np.array([[[int(z) for z in y.split(",")] for y in x.split(" -> ")] for x in data])

len(data)
#x1,y1 x2,y2


# filter to only horizontal and vertical lines
cords=np.array([x for x in data if x[0][0] == x[1][0] or x[0][1] == x[1][1]])

print(f"data: {len(data)}")
print(f"cords: {len(cords)}")

#get max x y cordinates
cordsMax=np.max(cords)
print(f"CordsMax: {cordsMax}")


# create map (zeros)
myMap=np.zeros([cordsMax+1,cordsMax+1])
print(f"mymap shape {myMap.shape}")


# draw lines


for x in cords:
    
    #The smallest value in the right place
    if x[0][0]<x[1][0]:
        x1=x[0][0]
        x2=x[1][0]
    else:
        x1=x[1][0]
        x2=x[0][0]
    
    if x[0][1]<x[1][1]:
        y1=x[0][1]
        y2=x[1][1]
    else:
        y1=x[1][1]
        y2=x[0][1]
    
    
    myMap[y1:y2+1,x1:x2+1]+=1



result=(myMap >= 2).sum()

print(f"Result: {result}")