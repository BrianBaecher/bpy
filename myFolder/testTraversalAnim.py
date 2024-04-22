import bpy
spawner = bpy.data.texts["spawn.py"].as_module()
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

def glowPulse(objectName, startFrame, duration, intensityChange, isRed):
    NO_EMISSION = 0.0
    RED = (1, 0, 0, 1)
    GREEN = (0, 1, 0, 1)

    obj = bpy.data.objects.get(objectName)
    objMat = obj.active_material.node_tree.nodes["Principled BSDF"]

    objMatEmissionColor = objMat.inputs[26]

    objMatEmissionColor.default_value = RED if isRed else GREEN

    objMatEmissionStrength = objMat.inputs[27]
    objMatEmissionStrength.default_value = NO_EMISSION

    objMatEmissionStrength.keyframe_insert(data_path="default_value", frame=startFrame)

    objMatEmissionStrength.default_value = intensityChange
    peakFrame = int(startFrame + (.5 * duration))

    objMatEmissionStrength.keyframe_insert(data_path="default_value", frame=peakFrame)

    endFrame = startFrame + duration
    objMatEmissionStrength.default_value = NO_EMISSION

    objMatEmissionStrength.keyframe_insert(data_path="default_value", frame=endFrame)


def setParticleEmitter(namesInCollection, startFrame):
    for name in namesInCollection:
        print(name)
        if name.find("EmitterSphere") != -1:
            bpy.context.view_layer.objects.active = bpy.data.objects.get(name)
            for m in bpy.context.active_object.modifiers:
                if m.type == "PARTICLE_SYSTEM":
                    ps = m.particle_system
                    ps.settings.frame_start = startFrame
                    ps.settings.frame_end = startFrame + 1


def rowWise3dTraverse(matrix, startFrame, frameStep, objectToAnimateName):
    frame = startFrame
    startPos = (0, 0, 10)
    bpy.context.view_layer.objects.active = bpy.data.objects.get(objectToAnimateName)
    obj = bpy.context.active_object
    obj.location = startPos
    obj.keyframe_insert(data_path="location", frame=frame)
    frame += frameStep

    for layer in matrix:
        for row in layer:
            for node in row:
                bpy.context.view_layer.objects.active = bpy.data.objects.get(objectToAnimateName)
                obj.location = node.getPos()
                obj.keyframe_insert(data_path="location", frame=frame)
                glowPulse(node.getName(), frame, 6, 2, True)
                setParticleEmitter(node.getEmitterNames(), frame)
                frame += frameStep


def colWise3dTraverse(matrix, frameStep, objectToAnimateName):
    frame = 0
    startPos = (0, 0, 10)
    bpy.context.view_layer.objects.active = bpy.data.objects.get(objectToAnimateName)
    obj = bpy.context.active_object
    obj.location = startPos
    obj.keyframe_insert(data_path="location", frame=frame)
    frame += frameStep

    for layer in matrix:
        depth = len(layer)
        for i in range(depth):
            for j in range(depth):  # width? right now m3 is square/cube so it's fine I think... but with a 5x3...
                node = layer[j][i]
                bpy.context.view_layer.objects.active = bpy.data.objects.get(objectToAnimateName)
                obj.location = node.getPos()
                obj.keyframe_insert(data_path="location", frame=frame)
                frame += frameStep
