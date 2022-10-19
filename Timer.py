import time 
import os, sys
# minutes ---------
print("Minutes?")
x = input()
minutesLeft = int(x)
# seconds ---------
print("Seconds?")
y = input()
secondsLeft = int(y)

q = ("Error, do not input negatives. 60 SEC = 1 MiNUTE RESTARTING...")
if (int(minutesLeft)) <= -1:
        print(q)
        time.sleep(2)
        os.execl(sys.executable, sys.executable, *sys.argv)
if(int(secondsLeft)) <= -1 :
        print(q)
        time.sleep(2)
        os.execl(sys.executable, sys.executable, *sys.argv)
if int(secondsLeft) >= 60:
        r = int(secondsLeft % 60)
        t = int(secondsLeft / 60)
        secondsLeft = r
        minutesLeft = minutesLeft + t

# this print is to clear all previous text
print("\n" * 20)
seconds = int(secondsLeft)
minutes = int(minutesLeft)
# timer ---------
while True:
        if seconds == 0:
                time.sleep(1)
                print(str(minutes) + ':00')
                minutes = minutes - 1
                seconds = seconds + 59          

        if seconds > 9:
                x = (str(minutes) + ':' + str(seconds))
        else:
                x = (str(minutes) + ':0' + str(seconds))     
        seconds = seconds - 1
        time.sleep(1)
        print(x)
        if (seconds, minutes) == 0:
                time.sleep(1)
                print('0:00')
                print('Timer Ended')
                quit()