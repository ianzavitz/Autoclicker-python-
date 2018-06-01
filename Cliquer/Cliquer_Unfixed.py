import time
import sys
import random
import pyautogui as p
import argparse
import statistics as s


parser = argparse.ArgumentParser()

parser.add_argument("n", help="Number of clicks",type=int)
parser.add_argument("-d", help="Delay between clicks", type=float)
parser.add_argument("--random",help="Enable Delay Variation/Randomization", default=False, action='store_const', const=True)

args = parser.parse_args()


#grab mouse position
#clickHub = p.position()

#assign number of clicks from arguments
n = args.n
#assign interclick delay, user input or default .5 second
if(args.d!=None):
    d = args.d
else:
    d = .5
print("No. Clicks: " + str(n))

#delay
print("Starting in 5 seconds...")
time.sleep(5)




history = [d]
i=0
while(i<n):
    #random delay addition of 0 to 1 second
    if(args.random):
        x = random.randint(0,100)/100
    else:
        x = 0
    #delay calculated
    delay = d + x
    #click then execute delay and record it's length in history
    p.click()
    time.sleep(delay)
    history.append(delay)
    if(len(history)>100):
        ave = s.mean(history)
        history = []
        for x in range(0, 9):
            history.append(ave)
    #print current click, average delay and last delay
    print("|: "+str(i+1) + " clicks :|: delay "+str(delay)[0:4]+ " :|: avg delay " + str(s.mean(history))[0:4]+":|              ",end="\r", flush=True)
    
    
    i+=1


print("\nEnding...")
sys.exit(0)
