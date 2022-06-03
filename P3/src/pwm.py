#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ###############################################
#
# program: pwm.py
# Controls brightness of a LED with pwm
#
# Autor: César Martínez
#        Lisset Noriega Domínguez
# License: MIT
#
# ## ###############################################


# Import Raspberry Pi's GPIO control library
import RPi.GPIO as GPIO
# Imports sleep functon
from time import sleep

led_PWM = 12
# Set up Rpi.GPIO library to use physical pin numbers
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_PWM, GPIO.OUT, initial=GPIO.LOW)

# Blink the led
pwmController = GPIO.PWM(led_PWM,100)
pwmController.start(0)

timeCycleOnOff = 1
timeWaiting = timeCycleOnOff/100

timeHolding = 0.5
while True:
    for i in range(100):
        pwmController.ChangeDutyCycle(i)
        sleep(timeWaiting)
    sleep(timeHolding)
    for i in range(100):
        pwmController.ChangeDutyCycle(100-i)
        sleep(timeWaiting)

pwmController.stop()
GPIO.cleanup()
