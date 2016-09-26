#!/usr/bin/python
#encoding=utf-8


# Push Bullet Notification
# the sensor has to be connected to pin 1 for power, pin 6 for ground
# and pin 7 for signal(board numbering!).


import time
import sys
import RPi.GPIO as GPIO
import requests
import json 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#API_Key From Push Bullet

API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' # Fill your API_Key from Push Bullet

def pushMessage(title, body):
	data = { 
	'type':'note',
	'title':title,
	'body':body }
	resp = requests.post('https://api.pushbullet.com/api/pushes',data=data,auth=(API_KEY,'')) 


def action(pin):
    print 'Sensor detected action!'
    pushMessage("Test message", "*****Alert****** Fire Deteced in Room *****Alert****** ")
    return

GPIO.add_event_detect(7, GPIO.RISING)
GPIO.add_event_callback(7, action)

try:
    while True:
        print 'alive'
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()
