## Cliquer -- Simple Python 3 Autoclicker 

# Installation

Clone this repository into the directory you wish to to run it from

Libraries used by this script: argparse, pyautogui, pynput
    
You may need to install some of the libraries with the command below, replacing library_name with the name of the needed library 
    
    $ pip install library_name
    or
    $ pip3 install library_name
    or 
    $ brew install libarary_name

# Use

Using the command line, navigate to the directory Cliquer is saved. 

The base command is $ python3 Cliquer.py n 

    n being the integer argument for the number of clicks you want. It is a manditory argument. 
    
    Optional arguments
        -d is the base delay between clicks in seconds (float)
        
        -r adds a random additional delay between (float) -r and (float) r in seconds
    
        --fixed, allowing the user to specify a fixed location on screen to click. 
        This allows for the user to do other tasks while the autoclicker is running, however the activity/window 
        the autoclicker is clicking must stay visible. 
        
        
       
To pause the script, use the shell command [control]-Z. To resume, type and enter fg. 
To end the script, use the shell command [control]-C
