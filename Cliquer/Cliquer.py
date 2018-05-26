import os
import sys
import argparse

#Cliquer

parser = argparse.ArgumentParser()
parser.add_argument("n", help="Number of clicks")
parser.add_argument("-d", help="Delay between clicks")
parser.add_argument("--fixed", help="Enable Fixed Click Location", default=False, action='store_const', const=True)
parser.add_argument("--random",help="Enable Delay Variation/Randomization", default=False, action='store_const', const=True)
args = parser.parse_args()

call = ''

#fixed or not?
if(args.fixed!=True):
    call+="python3 Cliquer_Unfixed.py " + args.n
else:
    call+="python3 Cliquer_Fixed.py " + args.n
    
#base delay specified?
if(args.d!=None):
    call+=" -d " + args.d

#varied/randomized delay or not?  
if(args.random==True):
    call+=" --random"
    
os.system(call)

sys.exit(0)
