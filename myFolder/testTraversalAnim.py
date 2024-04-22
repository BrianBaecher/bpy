import bpy

"""
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
"""

def rowWise3dTraverse(matrix, framestep, objectToAnimateName):
    # start at frame 0 fukit
    frame = 0
    startPos = (0, 0, 10)
    bpy.context.view_layer.objects.active = bpy.data.objects.get(objectToAnimateName)
    obj = bpy.context.active_object
    obj.location = startPos
    obj.keyframe_insert(data_path="location", frame=frame)
    frame += framestep

    for layer in matrix:
        for row in layer:
            for node in row:
                bpy.context.view_layer.objects.active = bpy.data.objects.get(objectToAnimateName)
                obj.location = node.getPos()
                obj.keyframe_insert(data_path="location", frame=frame)
                frame += framestep


def colWise3dTraverse(matrix, framestep, objectToAnimateName):
    # start at frame 0 fukit
    frame = 0
    startPos = (0, 0, 10)
    bpy.context.view_layer.objects.active = bpy.data.objects.get(objectToAnimateName)
    obj = bpy.context.active_object
    obj.location = startPos
    obj.keyframe_insert(data_path="location", frame=frame)
    frame += framestep

    for layer in matrix:
        depth = len(layer)
        for i in range(depth):
            for j in range(depth): #width? right now m3 is square/cube so it's fine I think... but with a 5x3...
                node = layer[j][i]
                bpy.context.view_layer.objects.active = bpy.data.objects.get(objectToAnimateName)
                obj.location = node.getPos()
                obj.keyframe_insert(data_path="location", frame=frame)
                frame += framestep
