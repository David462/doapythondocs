#D. Ayeni
#Get Current Position
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
while True:
    mc.setBlock(pos.x1, pos.y1 - 1, pos.z1, pos.x2, pos.y2, pos.z2, 1)
