from datetime import datetime, timezone
from pynput import keyboard
import time

# Version

version = '1.0.1'

# Variable inits

date_time = datetime.now(timezone.utc).strftime('%H:%MZ, %d/%m/%Y.')
key_press = False
key_press_counter = 0
timer_complete = False

# Functions

def countdown(time_sec):
    global date_time
    global key_press
    global timer_complete
    global timer_restart

    # Timer restart time
    timer_restart = datetime.now(timezone.utc).strftime('%H:%MZ, %d/%m/%Y.')

    # Timer loop

    while timer_complete == False:
        if key_press == True:       # Restart timer
            print('Key pressed. Restarting counter....', end ='\r')
            break
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print('Time remaining: {}                       '.format(timeformat), end='\r')
        for i in range(10):         # Restart timer during wait
            if key_press == True:
                print('Key pressed. Restarting counter....', end ='\r')
                break
            time.sleep(0.1)
        time_sec -= 1
        if mins == 0 and secs == 0: # Timer expiry
            timer_complete = True

def on_press(key):
    global key_press

    key_press = True
    
def on_release(key):
    global key_press
    global key_press_counter

    key_press = False
    key_press_counter +=1

# Main sequence

print('Thunder Timer v{}. Storm began at {}'.format(version, date_time))
time.sleep(0.5)
print('Press any key to restart timer.')
time.sleep(0.5)
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
counting_down = True
while counting_down == True:
    if timer_complete == True:
        counting_down = False
        break
    countdown((15*60))
print("The storm has passed. Last thunder heard at {}".format(timer_restart))

