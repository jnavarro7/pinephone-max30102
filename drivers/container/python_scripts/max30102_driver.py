"""
MIT License
Copyright (c) 2024 Jose Navarro
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Python script to read the pixels on the AMG8833 sensor which is a thermal imaging solution from Panasonic.
"""

import smbus
import time
import os
import curses
#from MAX30102_registers import * #Registers can be stored in a different file and imported here.

#Sensor is in I2C channel 3 
i2c_ch = 3

#MAX30102 address on the I2C bus
i2c_address = 

##MAX30102 Register addresses

#Status registers
INTSTATUS1 = 0x00  
INTSTATUS2 = 0x01
INTENABLE1 = 0x02
INTENABLE2 = 0x03

#FIFO registers
FIFOWRITEPOINTER = 0x04
OVERFLOWCOUNTER = 0x05
FIFOREADPOINTER = 0x06
FIFODATAREGISTER = 0x07

#Configuration registers
FIFOCONFIGURATION = 0x08
MODECONFIGURATION = 0x09
SPO2CONFIGURATION = 0x0A
RESERVED = 0x0B
LEDPULSEAMPLITUDE = 0x0C
RESERVED2 = 0X0E
RESERVED3 = 0x0F
MULTILEDMODECONTROL1 = 0x11
MULTILEDMODECONTROL2 = 0x12 

#I2C initialization
print("Initializing the I2C Bus")
bus = smbus.SMBus(i2c_ch)
time.sleep(1)

def debug_test():
	val = bus.read_i2c_block_data(i2c_address, pixeltest, 1)
	print("Test Value:", val)
	val = bus.read_byte_data(i2c_address, pixeltest)
	print(val)

def readpixels():
	# Read the Pixel 1 register (1 bytes)
	for i in pixel:
		val = bus.read_i2c_block_data(i2c_address, i)
		print("Value:", val)
		time.sleep(0.001)


def color_select(tempround):
	if tempround <= 22.0:
		return '\x1b[6;37;44m'
	elif tempround > 22.0 and tempround <= 24.0:
		return '\x1b[6;37;42m'
	elif tempround > 24.0 and tempround <= 36.0:
		return '\x1b[6;30;43m'
	elif tempround >= 36.0:
		return '\x1b[6;37;41m'
	else:
		return '\x1b[6;37;40m'

def readrows():
	for i in rows:
		for j in i:
			val = bus.read_byte_data(i2c_address, j)			#Read pixels from AMG8833 sensor
			valstr = str(val)									#Convert "val" to string
			dec = int(valstr, 16)								#Convert Hexadecimal to decimal
			temp = dec * 0.25									#Convert to Celcius degress
			tempround = round(temp,1)							#Round temperature to a single decimal point
			#print(tempround,end = " ")
			strtempround = str(tempround)						#Convert tempround to string
			#print('\x1b[6;37;44m' + strtempround + '\x1b[0m',end = " ")
			color = ""											#Define "color" variable as empty
			color = color_select(tempround)						#Function to assign a color depending on the temperature
			print(color + strtempround + '\x1b[0m',end = " ")	#Prints temperature in Celcius degress and color we have assigned depending on its range		
			time.sleep(0.001)
		print()


os.system("clear")			#Clean the terminal
while True:					#Run sensor pixels read and display 
	readrows()
	time.sleep(0.3)
	os.system("clear")

