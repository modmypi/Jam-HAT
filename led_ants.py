# Import the necessary libraries.
# gpiozero contains our JamHat object.
from gpiozero import JamHat
from time import sleep

# Initialise the JamHat object.
jh = JamHat()

# i is the counter for the LED row.
i = 0
# j is the counter for the LED column.
j = 0

# Setup a try/except block so we can run until CTRL+C is pressed.
try:
    while True:
        # Using modular arithmetic, decrease the light counter.
        # Our lights are in a matrix with rows 0-1 and columns 0-2.
        # Eg. [0][1] is the top yellow LED.
        if(j == 2):
            # If we're at the end of the column, increment to the next row.
            i = (i + 1) % 2
        # Increment the column.
        j = (j + 1) % 3
        sleep(0.2)
        # Turn the hat off.
        jh.off()
        # Turn on the LED at i j on the board.
        jh[i][j].on()
        
except KeyboardInterrupt:
    # If someone presses CTRL+C, close the JamHat, freeing of the Pins for use elsewhere.
    jh.close()