import bpy

spawner = bpy.data.texts["spawn.py"].as_module()
generator = bpy.data.texts["matrixGenerator.py"].as_module()
traverseKeyframer = bpy.data.texts["testTraverse.py"].as_module()


#nodesMatrix = generator.generate3d(generator.m3)

nodesMatrix = generator.createMatrix(3**3)

ballName = spawner.spawnBall()

bpy.context.view_layer.objects.active = bpy.data.objects.get(ballName)

traverseKeyframer.rowWise3dTraverse(nodesMatrix, 100, 5, bpy.context.active_object.name)
