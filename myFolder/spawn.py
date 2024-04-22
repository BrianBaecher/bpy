import bpy

storageFolderPath = r"C:\Users\brian\Desktop\blender_project\prefix\storage"


def spawnFromFile(path):
    with bpy.data.libraries.load(path) as (dataFrom, dataTo):
        dataTo.objects = [name for name in dataFrom.objects]

    for obj in dataTo.objects:
        bpy.context.scene.collection.objects.link(obj)
        return obj.name


def spawnBall():
    ballPath = storageFolderPath + r"\ball.blend"
    objName = spawnFromFile(ballPath)
    # adding emmision to ball material
    bpy.context.view_layer.objects.active = bpy.data.objects.get(objName)
    bpy.context.active_object.active_material.node_tree.nodes["Principled BSDF"].inputs[27].default_value = 10.3

    return objName


def spawnCollection(path):
    # Append the collection from the blend file
    with bpy.data.libraries.load(path, link=False) as (data_from, data_to):
        data_to.collections = [name for name in data_from.collections]

    # Instantiate the collection in the scene
    for collection in data_to.collections:
        for obj in collection.objects:
            bpy.context.collection.objects.link(obj.copy())

    # Return the names of the objects in the collection (optional)
    return [obj.name for obj in collection.objects]


def spawnEmitter():
    emitPath = storageFolderPath + r"\emit.blend"
    objNames = spawnCollection(emitPath)
    return objNames


def spawnNodeBall():
    path = storageFolderPath + r"\nodeBall.blend"
    objNames = spawnFromFile(path)
    bpy.context.view_layer.objects.active = bpy.data.objects.get(objNames)
    return objNames