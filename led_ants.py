from gpiozero import JamHat
from time import sleep

jh = JamHat()
i = 0
j = 0

try:
    while True:
        if(j == 2):
            i = (i + 1) % 2
        j = (j + 1) % 3
        sleep(0.2)
        jh.off()
        jh[i][j].on()
        
except:
    jh.close()