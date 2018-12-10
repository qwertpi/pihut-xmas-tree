from datetime import datetime
from random import randint,random
from gpiozero import LEDBoard
from time import sleep
#create an LEDBoard with all the pins for the LEDs on the tree bar the star LED which is controlled by the star code
tree = LEDBoard(*range(3,28),pwm=True)
while True:
    #picks a random number which will be used as an index for the led we will change
    r=randint(0,len(tree)-1)
    #store the brightness of the led with the index of r
    old=tree[r].value
    #change the brightness of the led with the index of r to a random number
    tree[r].value=(random())
    #sleep for half the diffrence between the old brightness and new brightness as a positive number
    sleep(abs(tree[r].value-old)/2)
