import random

import math

def cubic_root(n):
    return round(math.exp(math.log(n)/3), 6)


m3 = [
    [
    # layer 1
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ],

    [
    # layer 2
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
    ],

    [
    # layer 3
    [19, 20, 21],
    [22, 23, 24],
    [25, 26, 27]
    ],
]

notSequential = []

def randomList(numOfEls, intRangeLowerBound, intRangeUpperBound):
    list = []
    for i in range(numOfEls):
        list.append(random.randint(intRangeLowerBound, intRangeUpperBound))
    return list

def transformList(randList):
    length = len(randList)
    cubeRoot = int(cubic_root(len(randList)))
    print("IS CUBE")
    if length % cubeRoot == 0: # should mean a full cube, no missing spaces
        randList.sort()
        layerContainer = []
        partitioner = 0
        for layer in range(int(cubeRoot)):
            layerList = []
            for row in range(int(cubeRoot)):
                row = randList[partitioner : partitioner + cubeRoot]
                partitioner += cubeRoot
                layerList.append(row)
            layerContainer.append(layerList)
    return layerContainer

x = randomList(27, 1, 100)
x.sort()

x = transformList(x)

print(x)