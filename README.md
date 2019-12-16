## Cliquer -- Simple Python 3 Autoclicker 

# Installation

Clone this repository into the directory you wish to to run it from

Libraries used by this script: argparse, pyautogui, pynput

# Use

Using the command line, navigate to the directory Cliquer is saved. 

The base command is $ python3 Cliquer.py n 

    n being the integer argument for the number of clicks you want. It is a manditory argument. 
    
    Optional arguments
        -d is the base delay between clicks in seconds (float) default = 1
        
        -r adds a random additional delay between (float) -r and (float) r in seconds default = 0
    
        --fixed, allowing the user to specify a fixed location on screen to click. 
        This allows for the user to do other tasks while the autoclicker is running, however the activity/window 
        the autoclicker is clicking must stay visible. 
        
        --humanlike adds some randomized small variations (range of -.01 seconds to .01 seconds) in click location and randomized mouse movement times in fixed mode. 
        This is useful for autoclicking in games or other apps which frown on automation. It is not  perfect, given 
        the mouse movements are still often inhumanly fast. However if they were slower it would really work against the 
        idea of fixed mode allowing you to use your mouse while it autoclicks. 
        
        
       
To pause the script, use the shell command [control]-Z. To resume, type and enter fg. 
To end the script, use the shell command [control]-C
