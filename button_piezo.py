from gpiozero import JamHat
from time import sleep

jh = JamHat()

try:
    while True:
        if(jh.button_1.is_pressed):
            jh.buzzer.play(80)
        elif(jh.button_2.is_pressed):
            jh.buzzer.play(60)
        else:
            jh.off()
except:
    jh.close()
