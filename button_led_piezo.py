from gpiozero import JamHat
from time import sleep

jh = JamHat()

NOTES = [440.000, 391.995, 349.228, 329.628, 293.665, 261.626]
i = 0
j = 0
note = 0

try:
    while True:
        if(jh.button_2.is_pressed):
            note = (note + 1) % 6
            if(j == 2):
                i = (i + 1) % 2
            j = (j + 1) % 3
            sleep(0.1)
        jh.off()
        jh[i][j].on()

        if(jh.button_1.is_pressed):
            jh.buzzer.play(NOTES[note])
        sleep(0.1)

except KeyboardInterrupt:
    jh.close()
