__author__ = 'dfu3'

from Crypto.Cipher import AES
import base64
import os
from Crypto.Random import random
import  sys


from Tkinter import *

def playsound(frequency,duration):
    os.system('beep -f %s -l %s' % (frequency,duration))

root =  Tk()

sys.stdout.write('\a')
sys.stdout.flush()