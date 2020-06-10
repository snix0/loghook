import logging
import pyautogui

def foo():
    print("Hook entered")
    
# Follow a file like tail -f.

import time
from datetime import datetime

def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

if __name__ == '__main__':
    logfile = open("/tmp/game.log","r")
    loglines = follow(logfile)
    for line in loglines:
        if 'scale' in line:
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            filename = line.strip().replace(' ','_') + "_" + now + ".png"
            pyautogui.screenshot(filename)
            print("Saving screenshot to {}...".format(filename))
