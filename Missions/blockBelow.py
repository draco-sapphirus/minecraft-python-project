from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z
y = y + 10
mc.player.setTilePos(x, y, z)

time = 1

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
blockType = 46
mc.setBlock(x, y - 1, z, blockType)
