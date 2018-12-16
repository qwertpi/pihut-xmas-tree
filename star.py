from datetime import datetime
from time import sleep
from gpiozero import PWMLED
star = PWMLED(2)
#store christmas day in the current year in the c_day variable
c_day=datetime(datetime.now().year,12,25)

#subrotuine to advoid copy pasting code
def get_time():
    #get the current time down to the microsecond
    today = datetime.now()
    #find the difference between c_day and the time in the today variable
    rd = c_day-today
    #converts rd as a number of seconds to a string to so we can get only everything before the decimal point
    #then converts that to an integer and divides that integer by 500,000
    time=int(str(rd.total_seconds()).split(".")[0])/500000
    return time

while True:
    #turns the star on
    star.on()
    #waits for the amount of seconds returned by get_time
    sleep(get_time())
    #turns the star off
    star.off()
    #waits for the amount of seconds returned by get_time
    sleep(get_time())
