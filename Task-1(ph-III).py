import sys
import time

# defining countdown timer

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        sys.stdout.write(timer + '\r')
        sys.stdout.flush()
        time.sleep(1)
        t -= 1
    
    sys.stdout.write('Time up!\n')

# Change the timer_seconds value to set the countdown.

timer_seconds = 300 

countdown(timer_seconds)
