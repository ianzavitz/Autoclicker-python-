import time
import sys
import random
import pyautogui as p
import argparse
import statistics as s
from pynput import mouse,keyboard

#arguments
parser = argparse.ArgumentParser()
parser.add_argument("n", help="Number of clicks",type=int)
args = parser.parse_args()

#assign number of clicks from arguments
n = args.n
print("No. Clicks: " + str(n))

#when mouse clicked
def on_click(x, y, button, pressed):
    if pressed:

        #grab mouse position
        clickHub = p.position()

        #delay
        print("Starting in 5 seconds...")
        time.sleep(5)

        #history stores values for average time
        history = [2]
        i=0
        while(i<n):
            x = random.randint(0,200)/200
    
            delay = 0.60 + x
            returnPosition = p.position()
            p.click(x=clickHub[0],y=clickHub[1])
            p.moveTo(returnPosition[0],returnPosition[1],(x/10))
            time.sleep(delay)
            history.append(delay+x/10)
            if(len(history)>60):
                ave = s.mean(history)
                history = []
                for x in range(0, 9):
                    history.append(ave)
            print("|: "+str(i+1) + " clicks :|: delay "+str(delay+x/10)[0:4]+ " :|: avg delay " + str(s.mean(history))[0:4]+":|              ",end="\r", flush=True)
            i+=1


        print("\nEnding...")
        sys.exit(0)

    if not pressed:
        # Stop listener
        return False


# Collect events until released
print("Pick clicking location")
with mouse.Listener(on_click=on_click) as listener:
    listener.join()

