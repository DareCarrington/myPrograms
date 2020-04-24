#The sad program
import webbrowser
import os
import random
import string
import json
import time


loveSongs = json.loads(open('loveSongs.json').read())
mikaylaSad = True
def sad():
    return mikaylaSad
def makeHappy():
    mikaylaSad = False
def beAwesome():
    print("I love you sexy keep doing you!!! Your gonna be the most badass dietitian ever!!! I love you to the moon and back now enjoy this song cutie!")
    time.sleep(5)
    return webbrowser.open(random.choice(loveSongs))
    
    
while True:
    print("Are you sad?(y/n)")
    if(input() == "y"):
        mikaylaSad = True
    else:
        print("Keep doing you BOO BOO\n\n")
    if(sad() == True):
        makeHappy()
        beAwesome()
        print("\n\n")
        
    mikaylaSad = False