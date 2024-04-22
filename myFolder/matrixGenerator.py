import bpy
import random
import math

spawn = bpy.data.texts["spawn.py"].as_module()


class Node:
    def __init__(self, idNum):
        self.id = idNum

    def setPos(self, posTuple):
        self.posTuple = posTuple
        self.xpos = posTuple[0]
        self.ypos = posTuple[1]
        self.zpos = posTuple[2]

    def setLayer(self, layerNum):
        self.layer = layerNum

    def setName(self, name):
        self.name = name

    def setEmitterNames(self, listOfNames):
        self.emitterNames = listOfNames

    def getPos(self):
        return self.posTuple

    def getLayer(self):
        return self.layer

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def getEmitterNames(self):
        return self.emitterNames


m3 = [
    [
        # layer 1
        [Node(1), Node(2), Node(3)],
        [Node(4), Node(5), Node(6)],
        [Node(7), Node(8), Node(9)]],

    [
        # layer 2
        [Node(10), Node(11), Node(12)],
        [Node(13), Node(14), Node(15)],
        [Node(16), Node(17), Node(18)]],

    [
        # layer 3
        [Node(19), Node(20), Node(21)],
        [Node(22), Node(23), Node(24)],
        [Node(25), Node(26), Node(27)]],
]


def cubic_root(n):
    return round(math.exp(math.log(n)/3), 6)


def generate3d(threeDimList):
    for layerNum, layer in enumerate(threeDimList):
        y = layerNum * 5
        for rowNum, row in enumerate(layer):
            z = rowNum * -5
            x = 0
            for node in row:
                # bpy.ops.mesh.primitive_uv_sphere_add(radius=1, enter_editmode=False, align='WORLD', location=(x, y, z),
                #                                  scale=(1, 1, 1))
                nodeBallName = spawn.spawnNodeBall()
                bpy.context.view_layer.objects.active = bpy.data.objects.get(nodeBallName)
                bpy.context.active_object.location = (x,y,z)
                node.setLayer(layerNum)
                node.setPos((x, y, z))
                node.setName(bpy.context.active_object.name)

                emitterNames = spawn.spawnEmitter()
                node.setEmitterNames(emitterNames)
                for name in emitterNames:
                    obj = bpy.data.objects.get(name)
                    obj.location = (x, y, z)
                x += 5
                print(node.id, bpy.context.active_object.name)
    return threeDimList


def randomList(numOfEls, intRangeLowerBound, intRangeUpperBound):
    list = []
    for i in range(numOfEls):
        list.append(Node(random.randint(intRangeLowerBound, intRangeUpperBound)))
    return list


def transformList(randList):
    length = len(randList)
    cubeRoot = cubic_root(len(randList))
    if length % cubeRoot == 0: # should mean a full cube, no missing spaces
        print("IS CUBE")
        list.sort(randList, key= lambda node: node.getId())
        layerContainer = []
        partitioner = 0
        for layer in range(int(cubeRoot)):
            layerList = []
            for row in range(int(cubeRoot)):
                row = randList[partitioner : partitioner + int(cubeRoot)]
                partitioner += int(cubeRoot)
                layerList.append(row)
            layerContainer.append(layerList)
        return layerContainer
    else:
        print("number of elements is not cube root-able :|")
        return None


def createMatrix(numOfElements, randIntRangeLowerBound = None, randIntRangeUpperBound = None):
    mtx = None
    if randIntRangeLowerBound is not None and randIntRangeUpperBound is not None:
        nodes = randomList(numOfElements, randIntRangeLowerBound, randIntRangeUpperBound)
        formattedNodes = transformList(nodes)
        if formattedNodes is not None:
            return generate3d(formattedNodes)
    else:
        nodes = []
        for i in range(numOfElements):
            nodes.append(Node(i))
        nodes = transformList(nodes)

        if nodes is not None:
            return generate3d(nodes)

