import bpy
import serial
import mathutils
from time import sleep

objSerial = serial.Serial("COM3",9600)
line = objSerial.readline()
print(line)