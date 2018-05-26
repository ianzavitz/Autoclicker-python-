## Cliquer -- Simple Python 3 Autoclicker 

# Installation

Clone this repository into the directory you wish to to run it from

Libraries used by this script: os, sys, time, random, statistics, argparse, pyautogui, pynput
    
You may need to install some of the libraries with the command below
    
    $ pip install library_name
    or
    $ pip3 install library_name
    or 
    $ brew install libarary_name

# Use

Using the command line, navigate to the directory Cliquer is saved. 

The base command is $ python3 Cliquer.py n 

    n being the argument for the number of clicks you want. It is a manditory argument. 
    
    Optional arguments
        -d is the base delay between clicks
    
        --fixed, allowing the user to specify a fixed location on screen to click. 
        This allows for the user to do other tasks while the autoclicker is running, however the activity/window 
        the autoclicker is clicking must stay visible. 
        
        --random adds a random additional delay between clicks between 0 and 1 second
        
        
    
    
