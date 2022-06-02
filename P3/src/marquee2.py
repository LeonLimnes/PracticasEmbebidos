#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ###############################################
#
# marquee.py
# Blinks a led on pin 32 using Raspberry Pi
#
# Autor: César Martínez
# License: MIT
#
# ## ###############################################


# Import Raspberry Pi's GPIO control library
import RPi.GPIO as GPIO
# Imports sleep functon
from time import sleep
# Initializes virtual board (comment out for hardware deploy)
#import virtualboard

#Arreglo de pines para leds
leds_array = [12,16,18,22,24,26,32]
# Set up Rpi.GPIO library to use physical pin numbers
GPIO.setmode(GPIO.BOARD)
for led in leds_array:
    GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)

# Blink the led

while True:
    n = float(input("Velocidad: (se recomienda de 0.1 a 10):"))
    for led in reversed(leds_array):
        GPIO.output(led, GPIO.HIGH)
        sleep(n)
        GPIO.output(led, GPIO.LOW)