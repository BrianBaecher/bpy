import bpy

spawn = bpy.data.texts["spawn.py"].as_module()
generator = bpy.data.texts["matrixGenerator.py"].as_module()
traverseKeyframer = bpy.data.texts["testTraverse.py"].as_module()


#nodesMatrix = generator.generate3d(generator.m3)

nodesMatrix = generator.createMatrix(3**3)

ballName = spawn.spawnBall()

bpy.context.view_layer.objects.active = bpy.data.objects.get(ballName)

traverseKeyframer.colWise3dTraverse(nodesMatrix, 10, bpy.context.active_object.name)
