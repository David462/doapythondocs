#D. Ayeni
#Places a randomly colored wool block

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pos = mc.player.getTilePos()

def randWool():
    color = random.randint(0, 15)
    if color == 0:
        mc.setBlock(pos.x + 1, pos.y, pos.z, 35, 0)
    elif color == 1:
        mc.setBlock(pos.x + 1, pos.y, pos.z, 35, 1)
    elif color == 2:
        mc.setBlock(pos.x + 1, pos.y, pos.z, 35, 2)
    elif color == 3:
        mc.setBlock(pos.x + 1, pos.y, pos.z, 35, 3)
    elif color == 4:
        mc.setBlock(pos.x + 1, pos.y, pos.z, 35, 4)
    elif color == 5:
        mc.setBlock(pos.x + 1, pos.y, pos.z, 35, 5)
    elif color == 6:
        mc.setBlock(pos.x + 1, pos.y, pos.z, 35, 6)
    elif color == 7:
        mc.setBlock(pos.x + 1, pos.y, pos.z, 35, 7)
    elif color == 8:
        mc.setBlock(pos.x + 1, pos.y, pos.z, 35, 8)
    elif color == 9:
        mc.setBlock(pos.x + 1, pos.y, pos.z, 35, 9)
    elif color == 10:
        mc.setBlock(pos.x + 1, pos.y, pos.z, 35, 10)
    elif color == 11:
        mc.setBlock(pos.x + 1, pos.y, pos.z, 35, 11)
    elif color == 12:
        mc.setBlock(pos.x + 1, pos.y, pos.z, 35, 12)
    elif color == 13:
        mc.setBlock(pos.x + 1, pos.y, pos.z, 35, 13)
    elif color == 14:
        mc.setBlock(pos.x + 1, pos.y, pos.z, 35, 14)
    elif color == 15:
        mc.setBlock(pos.x + 1, pos.y, pos.z, 35, 15)

while True:
    if GPIO.input(6) == GPIO.LOW:
        randWool()