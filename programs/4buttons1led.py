import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(38, GPIO.OUT, GPIO.LOW)
# Set pin 10 to be aninput pin and set intial value to be
# pulled low (off)
LEDlit = False
while True:
    if GPIO.input(10) == GPIO.HIGH:
        print("First button pressed")
        if LEDlit == True:
            LEDlit = False
            GPIO.output(38, GPIO.HIGH)
        else:
            LEDlit = True
            GPIO.output(38, GPIO.LOW)
    elif GPIO.input(16) == GPIO.HIGH:
        print("Second button pressed")
    elif GPIO.input(22) == GPIO.HIGH:
        print("Third button pressed")
    elif GPIO.input(28) == GPIO.HIGH:
        print("Fourth button pressed")
            