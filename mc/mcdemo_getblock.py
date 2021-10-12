#D. Ayeni
#Get block info
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()

getBlock = mc.getBlock(pos.x, pos.y - 1, pos.z)
if getBlock == 57