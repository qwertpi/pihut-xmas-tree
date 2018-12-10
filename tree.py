from datetime import datetime
from random import randint,random
from gpiozero import LEDBoard
from time import sleep
tree = LEDBoard(*range(3,28),pwm=True)
tree.off()
tree.on()
sleep(5)
while True:
    r=randint(0,len(tree)-1)
    old=tree[r].value
    tree[r].value=(random())
    sleep(abs(tree[r].value-old)/2)
