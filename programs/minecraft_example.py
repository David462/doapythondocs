#D. Ayeni
#Minecraft Code Example

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

mc.postToChat(mc.player.getTilePos())

