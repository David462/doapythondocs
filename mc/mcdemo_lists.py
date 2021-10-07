#D. Ayeni
#Places a randomly colored wool block

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)# Button Setup

pos = mc.player.getTilePos()

woolColors = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def placeNext(direc):
    counter = 0
    counter = counter + direc
    if counter > 2:
        counter = 0
    elif counter < 0:
        counter = 2
    mc.setBlock(pos.x, pos.y, pos.z, 35, woolColors[counter])

while True:
    if GPIO.input(6) == GPIO.LOW:
        placeNext(1)
    elif GPIO.input(13) == GPIO.LOW:
        placeNext(-1)
