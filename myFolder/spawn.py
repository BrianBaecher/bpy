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
    return objName