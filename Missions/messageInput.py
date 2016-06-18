from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
me1 = ("Bob:")
me2 = ("Hello bob1")

mc.postToChat(me1 + me2)

mes = "I know who you are"
me = "I know were you live"

time.sleep(3)
mc.postToChat(mes)

time.sleep(3)
mc.postToChat(me)
