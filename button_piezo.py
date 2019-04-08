# Import the necessary libraries.
# gpiozero contains our JamHat object.
from gpiozero import JamHat
from time import sleep

# Initialise the JamHat object.
jh = JamHat()

# Setup a try/except block so we can run until CTRL+C is pressed.
try:
    while True:
        if(jh.button_1.is_pressed):
            # If the button on the left is pressed, beep midi note 80.
            jh.buzzer.play(80)
        elif(jh.button_2.is_pressed):
            # If the button on the right is pressed, beep midi note 60.
            jh.buzzer.play(60)
        else:
            # Turn off the buzzer.
            jh.off()
except KeyboardInterrupt:
    # If someone presses CTRL+C, close the JamHat, freeing of the Pins for use elsewhere.
    jh.close()
