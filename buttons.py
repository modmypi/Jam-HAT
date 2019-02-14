from gpiozero import JamHat
from time import sleep

jh = JamHat()

try:
    counter = 0
    while True:
        if jh.button_1.is_pressed or jh.button_2.is_pressed:
            if jh.button_1.is_pressed:
                counter += 1
                jh.button_1.wait_for_release()
            if jh.button_2.is_pressed:
                counter -= 1
                jh.button_2.wait_for_release()
            print("Counter: %d" % counter)
        sleep(0.1)
except:
    jh.close()
