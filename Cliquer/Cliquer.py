import os
import sys
import argparse

#Cliquer

parser = argparse.ArgumentParser()
parser.add_argument("n", help="Number of clicks")
parser.add_argument("--fixed", help="Enable Fixed Click Location", default=False, action='store_const', const=True)
args = parser.parse_args()

n = args.n

if(args.fixed!=True):
    os.system("python3 Cliquer_Unfixed.py " + n)
else:
    os.system("python3 Cliquer_Fixed.py " + n)
    
sys.exit(0)