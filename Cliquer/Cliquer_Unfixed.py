import time
import sys
import random
import pyautogui as p
import argparse
import statistics as s


parser = argparse.ArgumentParser()

parser.add_argument("n", help="Number of clicks",type=int)

args = parser.parse_args()


#grab mouse position
#clickHub = p.position()

#number of clicks
n = args.n

print("No. Clicks: " + str(n))

#delay
print("Starting in a moment...")
time.sleep(5)




history = [2]
i=0
while(i<n):
    x = random.randint(0,200)/200
    
    delay = 0.60 + x
    p.click()
    time.sleep(delay)
    history.append(delay)
    if(len(history)>60):
        ave = s.mean(history)
        history = []
        for x in range(0, 9):
            history.append(ave)
    print("|: "+str(i+1) + " clicks :|: delay "+str(delay)[0:4]+ " :|: avg delay " + str(s.mean(history))[0:4]+":|              ",end="\r", flush=True)
    
    
    i+=1


print("\nEnding...")
sys.exit(0)