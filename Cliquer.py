#This script created by Ian Zavitz

import time
import sys
import random
import pyautogui as pyag
import argparse
import statistics as stat
from pynput import mouse,keyboard

parser = argparse.ArgumentParser()
parser.add_argument("n", help="Number of clicks",type=int)
parser.add_argument("-d", help="Delay between clicks (seconds)", type=float, default=1)
parser.add_argument("-r",help="Randomization (seconds)", type=float, default=0)
parser.add_argument("--fixed", help="Enable Fixed Click Location", default=False, action='store_const', const=True)
parser.add_argument("--humanlike", help="Adds some slight variation to clicking locations and mouse movement speed", default=False, action='store_const', const=True)

args = parser.parse_args()

loc = None
if(args.fixed is True):
    print("Cliquer: Click starting location to begin")
else:
    print("Cliquer: Click anywhere to begin")

def on_click(x, y, button, pressed):
    if pressed:
        class fixed_click(object):
            def __init__(self, n, d, r, loc):
                delay_log = []
                for i in range(n):
                    #calculate delay with randomization
                    rand_ratio = random.randint(-100,100)/100
                    if(args.humanlike==True):
                        rand_ratio_2 = random.randint(-100,100)/100
                        rand_ratio_3 = random.randint(-100,100)/100
                    rand_adj = rand_ratio * r
                    delay = d + rand_adj
                    #natural mouse position recorded
                    return_pos = pyag.position()
                    #click and then move back to natural mouse position
                    #if human-like is selected this will add a random, small movement in x and y
                    if(args.humanlike==True):
                        pyag.moveTo(loc[0]+rand_ratio_2/100, loc[1]+rand_ratio_3/100, duration=rand_ratio/10)
                    else:
                        pyag.moveTo(loc[0],loc[1])
                    pyag.click()
                    pyag.moveTo(return_pos[0], return_pos[1], duration=rand_ratio*2/10)
                    #process delay and record it in delay_log
                    time.sleep(delay)
                    if(len(delay_log)==0):
                        delay_log = [delay]
                    else:
                        delay_log.append(delay)
                    if(len(delay_log)>=1000):
                        delay_log = []
                        for _ in range(0, 9):
                            delay_log.append(stat.mean(delay_log))
                    #print current click, average delay length and most current delay length
                    print("|: "+str(i+1) + " clicks :|: delay "+str(delay)[0:4]+ " :|: avg delay " + str(stat.mean(delay_log))[0:4]+":|              ",end="\r", flush=True)
                print("\nEnding...")
                sys.exit(0)

        class click(object):
            def __init__(self, n, d, r):
                delay_log = []
                for i in range(n):
                #calculate delay with randomization
                    rand_ratio = random.randint(-100,100)/100
                    rand_adj = rand_ratio * r
                    delay = d + rand_adj
                    
                    #click
                    pyag.click()
                    #process delay and record it in delay_log
                    time.sleep(delay)
                    if(len(delay_log)==0):
                        delay_log = [delay]
                    else:
                        delay_log.append(delay)
                    if(len(delay_log)>=1000):
                        delay_log = []
                        for _ in range(0, 9):
                            delay_log.append(stat.mean(delay_log))
                    #print current click, average delay length and most current delay length
                    print("|: "+str(i+1) + " clicks :|: delay "+str(delay)[0:4]+ " :|: avg delay " + str(stat.mean(delay_log))[0:4]+":|              ",end="\r", flush=True)
                print("\nCliquer: Complete")
                sys.exit(0)
        if(args.fixed is True):
            loc = pyag.position()
            fixed_click(args.n, args.d, args.r, loc)
        else:
            click(args.n, args.d, args.r)

        

    if not pressed:
        loc = None
        return False

with mouse.Listener(on_click=on_click) as listener:
    listener.join()
'''
class fixed_click(object):
    def __init__(self, n, d, r, loc):
        delay_log = []
        for i in range(n):
            
            #calculate delay with randomization
            rand_ratio = random.randint(-100,100)/100
            rand_adj = rand_ratio * r
            delay = d + rand_adj
            
            #natural mouse position recorded
            returnPos = p.position()
            #click and then move back to natural mouse position
            p.click(x=loc[0],y=loc[1])
            p.moveTo(return_pos[0],return_pos[1])
            #process delay and record it in delay_log
            time.sleep(delay)
            if(len(delay_log)==0):
                delay_log = [delay]
            else:
                delay_log.append(delay)
            if(len(delay_log)>=1000):
                delay_log = []
                for x in range(0, 9):
                    delay_log.append(stat.mean(delay_log))
            #print current click, average delay length and most current delay length
            print("|: "+str(i+1) + " clicks :|: delay "+str(delay)[0:4]+ " :|: avg delay " + str(s.mean(history))[0:4]+":|              ",end="\r", flush=True)

        print("\nEnding...")
        sys.exit(0)

class click(object):
    def __init__(self, n, d, r):
        delay_log = []
        for i in range(n):
            
            #calculate delay with randomization
            rand_ratio = random.randint(-100,100)/100
            rand_adj = rand_ratio * r
            delay = d + rand_adj
            
            #click
            p.click()
            #process delay and record it in delay_log
            time.sleep(delay)
            if(len(delay_log)==0):
                delay_log = [delay]
            else:
                delay_log.append(delay)
            if(len(delay_log)>=1000):
                delay_log = []
                for x in range(0, 9):
                    delay_log.append(stat.mean(delay_log))
            #print current click, average delay length and most current delay length
            print("|: "+str(i+1) + " clicks :|: delay "+str(delay)[0:4]+ " :|: avg delay " + str(s.mean(history))[0:4]+":|              ",end="\r", flush=True)
        
        print("\nEnding...")
        sys.exit(0)
'''
