from datetime import datetime
from time import sleep
from random import randint,random
from gpiozero import PWMLED
star = PWMLED(2)
print("off")
star.off()
sleep(2)
print("On")
while True:
    today = datetime.now()
    rd = datetime(datetime.now().year,12,25)-today
    time=int(str(rd.total_seconds()).split(".")[0])/500000
    star.on()
    sleep(time)
    star.off()
    sleep(time)
