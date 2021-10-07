#D. Ayeni
#How to place a house with a button
from mcpi.minecraft import Minecraft
mc = Minecraft.create()



#Setup for button
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
#Set up each pin number
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
def house():
    pos = mc.player.getTilePos()
    #The overall build of the house
    mc.setBlocks(pos.x + 1, pos.y, pos.z + 1,
                 pos.x + 6, pos.y + 5, pos.z + 6, 5)
    #Empty Space in the house
    mc.setBlocks(pos.x + 2, pos.y + 1, pos.z + 2,
                 pos.x + 5, pos.y + 4, pos.z + 5, 0)
    #Door
    mc.setBlocks(pos.x + 3, pos.y + 1, pos.z + 1,
                 pos.x + 3, pos.y + 2, pos.z + 1, 64)
    #Window
    mc.setBlocks(pos.x + 4, pos.y + 2, pos.z + 1,
                 pos.x + 5, pos) 
    
while True:
    if GPIO.input(6) == GPIO.LOW:
        house()
        
    