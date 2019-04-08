# Import the necessary libraries.
# gpiozero contains our JamHat object.
from gpiozero import JamHat
from time import sleep

# Initialise the JamHat object.
jh = JamHat()

# Setup a try/except block so we can run until CTRL+C is pressed.
try:
    # Initialise counter
    counter = 0
    while True:
        if jh.button_1.is_pressed or jh.button_2.is_pressed:
            # If either button is pressed...
            if jh.button_1.is_pressed:
                # If the left button is pressed, increment the counter.
                counter += 1
                # Wait until the button is released before moving on.
                jh.button_1.wait_for_release()
            if jh.button_2.is_pressed:
                # If the right button is pressed, increment the counter.
                counter -= 1
                # Wait until the button is released before moving on.
                jh.button_2.wait_for_release()
            # Print out the counter value to the screen.
            print("Counter: %d" % counter)
        sleep(0.1)
except KeyboardInterrupt:
    # If someone presses CTRL+C, close the JamHat, freeing of the Pins for use elsewhere.
    jh.close()
