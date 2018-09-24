#!/usr/bin/env python
import sys
from subprocess import Popen, PIPE
from pyautogui import *
from time import sleep
import pymsgbox
#from tendo import singleton
#import tendo.tee
#me = singleton.SingleInstance() # will sys.exit(-1) if other instance is runnin
#SingleInstance force


p = Popen(['start','/wait','cmd'],shell=True)

if len(sys.argv) > 1 :
    with open('logCmdInput.txt','w') as f:
    	for i in range(0,len(sys.argv)):
    		f.write(sys.argv[i]+'\n')
else:
    pymsgbox.alert('ningun comando ha sido pasado')

sleep(4.5)

moveTo(300,300)
click()
typewrite('Write Something')
press('enter')
