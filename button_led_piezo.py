# Import the necessary libraries.
# gpiozero contains our JamHat object.
from gpiozero import JamHat
from time import sleep

# Initialise the JamHat object.
jh = JamHat()

# Build an array of notes in hertz.
NOTES = [440.000, 391.995, 349.228, 329.628, 293.665, 261.626]

# Initialise our counters for the while loop below.
i = 0
j = 0
note = 0

# Setup a try/except block so we can run until CTRL+C is pressed.
try:
    while True:
        if(jh.button_2.is_pressed):
            # If the second button is pressed, increment the counter into our NOTES array.
            note = (note + 1) % 6
            # Using modular arithmetic, decrease the light counter.
            # Our lights are in a matrix with rows 0-1 and columns 0-2.
            # Eg. [0][1] is the top yellow LED.
            if(j == 2):
                # If we're at the end of the row, increment to the next row.
                i = (i + 1) % 2
            # Increment the column.
            j = (j + 1) % 3
            sleep(0.1)
        # Turn off the hat
        jh.off()
        # Turn on the next light in the i/jth slot.
        jh[i][j].on()

        if(jh.button_1.is_pressed):
            # If the button is pressed, play the current note from NOTES out of the buzzer.
            jh.buzzer.play(NOTES[note])
        sleep(0.1)

except KeyboardInterrupt:
    # If someone presses CTRL+C, close the JamHat, freeing of the Pins for use elsewhere.
    jh.close()
