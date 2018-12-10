from datetime import datetime
from time import sleep
from gpiozero import PWMLED
star = PWMLED(2)
while True:
    #get the current time down to the microsecond
    today = datetime.now()
    #find the diffrence between christmas day in the current year and the time in the today variable
    rd = datetime(datetime.now().year,12,25)-today
    #converts rd as a number of seconds to a string to so we can get only everyhting before the decimal point and then converts that to an integer and divides that integer by 500,000
    time=int(str(rd.total_seconds()).split(".")[0])/500000
    #turns the star on
    star.on()
    #waits for the amount of seconds in time
    sleep(time)
    #turns the star off
    star.off()
    #waits for the amount of seconds in time
    sleep(time)
