from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = -1
y = 66
z = 14
BlockType = 43
for i in range(0, 300):
    mc.setBlock(x, y + i, z, BlockType)
