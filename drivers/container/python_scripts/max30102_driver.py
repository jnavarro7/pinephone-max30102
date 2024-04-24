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

Python script to drive the MAX30102 pulse oximeter & heart-rate monitor sensor.
"""

import smbus
import time
import os
import curses
#from MAX30102_registers import * #Registers can be stored in a different file and imported here.

#Sensor is in I2C channel 3 
i2c_ch = 3

#MAX30102 address on the I2C bus
read_i2c_address = 0xAF
write_i2c_address = 0xAE

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

#Reserved
RESERVED_01 = 0x13
RESERVED_02 = 0x14
RESERVED_03 = 0x14
RESERVED_04 = 0x15 
RESERVED_05 = 0x16
RESERVED_06 = 0x17
RESERVED_07 = 0x18
RESERVED_08 = 0x19
RESERVED_09 = 0x1A
RESERVED_10 = 0x1B
RESEVERD_11 = 0x1C
RESERVED_12 = 0x1D
RESERVED_13 = 0x1E

#Die temperature
DIE_TEMP_INT = 0x20
DIE_TEMP_FRACTION = 0x21
DIE_TEMP_CONFIG = 0x22
#Die temperature reserved
DIE_TEMP_RESERVED_01 = 0x23
DIE_TEMP_RESERVED_02 = 0x24
DIE_TEMP_RESERVED_03 = 0x25
DIE_TEMP_RESERVED_04 = 0x26
DIE_TEMP_RESERVED_05 = 0x27
DIE_TEMP_RESERVED_06 = 0x28
DIE_TEMP_RESERVED_07 = 0x29
DIE_TEMP_RESERVED_08 = 0x2A
DIE_TEMP_RESERVED_09 = 0x2B
DIE_TEMP_RESERVED_10 = 0x2C
DIE_TEMP_RESERVED_11 = 0x2D
DIE_TEMP_RESERVED_12 = 0x2E
DIE_TEMP_RESERVED_13 = 0x2F

#Part ID
REV_ID = 0xFE
PART_ID = 0xFF

#I2C initialization
print("Initializing the I2C Bus")
bus = smbus.SMBus(i2c_ch)
time.sleep(1)


while True:				

