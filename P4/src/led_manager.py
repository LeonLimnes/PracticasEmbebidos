# !/usr/bin/env python3
# ## ###############################################
#
# led_manager.py
# Controls leds in the GPIO
#
# Autor: Pérez Gutiérrez Sandra
# License: MIT
#
# ## ###############################################

# Future imports (Python 2.7 compatibility)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import Raspberry Pi's GPIO control library
import RPi.GPIO as GPIO
# Imports sleep functon
from time import sleep
# Initializes virtual board (comment out for hardware deploy)
#import virtualboard


#Array con los pines de los leds
leds_array = [12,16,18,22,24,26,32]

disp_array = [36,37,38,40]

# Set up Rpi.GPIO library to use physical pin numbers
GPIO.setmode(GPIO.BOARD)
for led in leds_array:
    GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)
for disp in disp_array:
    GPIO.setup(disp, GPIO.OUT, initial=GPIO.LOW)


#Casos para encender los LEDS
def leds(num):
        for led in leds_array:
            GPIO.output(led, GPIO.LOW)  # Turn led off
        if num == 7:
            print("CLiked")
            GPIO.output(32, GPIO.HIGH)  # Turn led

        if num == 6:
            GPIO.output(26, GPIO.HIGH)  # Turn led

        if num == 5:
            GPIO.output(24, GPIO.HIGH)  # Turn led

        if num == 4:
            GPIO.output(22, GPIO.HIGH)  # Turn led

        if num == 3:
            GPIO.output(18, GPIO.HIGH)  # Turn led

        if num == 2:
            GPIO.output(16, GPIO.HIGH)  # Turn led

        if num == 1:
            GPIO.output(12, GPIO.HIGH)  # Turn led



def bcd(num):
		GPIO.output(36,GPIO.HIGH if (num & 0x00000001)  > 0 else GPIO.LOW)
		GPIO.output(38, GPIO.HIGH if (num & 0x00000002) > 0 else GPIO.LOW)
		GPIO.output(40, GPIO.HIGH if (num & 0x00000004) > 0 else GPIO.LOW)
		GPIO.output(37, GPIO.HIGH if (num & 0x00000008) > 0 else GPIO.LOW)	



def marquee(type='pingpong'):
	switcher = {
		'left'     : _marquee_left,
		'right'    : _marquee_right,
		'pingpong' : _marquee_pingpong
	}
	func = switcher.get(type, None)
	if func:
		func()


def _marquee_right():
    for led in leds_array:
        GPIO.output(led, GPIO.LOW)  # Turn led off
    for led in leds_array:
        GPIO.output(led, GPIO.HIGH)  # Turn led off
        sleep(0.1)
        GPIO.output(led, GPIO.LOW)  # Turn led
def _marquee_left():
    for led in leds_array:
        GPIO.output(led, GPIO.LOW)  # Turn led off
    for led in leds_array[::-1]:
        GPIO.output(led, GPIO.HIGH)  # Turn led off
        sleep(0.1)
        GPIO.output(led, GPIO.LOW)  # Turn led

def _marquee_pingpong():
	_marquee_right()
	_marquee_left()