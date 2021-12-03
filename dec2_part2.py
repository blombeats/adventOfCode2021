import numpy as np



with open("dec2_input.txt", "r") as f:
    data = f.readlines()

data = [x.split() for x in data if x]  # remove endline (there's a better way to do this, but I'm lazy)
data = [[x[0],int(x[1])] for x in data] #convert numbers to int

print(f"Data length: {len(data)}")

horizontal=0
depth=0
aim=0
skips=0

for a,n in data: #angle, n
    a=a.strip().lower() #just in case

    if a=="down":
        aim+=n
    elif a=="up":
        aim -= n
    elif a=="forward":
        horizontal+=n
        depth+=n*aim
    else:
        skips+=1

print(f"Horizontal: {horizontal}")
print(f"Depth: {depth}")
print(f"skips: {skips}")


print(f"Answer: {horizontal*depth}")


"""
Data length: 1000
Horizontal: 1996
Depth: 1022
skips: 0
Answer: 2039912
"""
