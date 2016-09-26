#!/usr/bin/python
#encoding=utf-8


# Twilio Bullet Notification
# the sensor has to be connected to pin 1 for power, pin 6 for ground
# and pin 7 for signal(board numbering!).


import time
import sys
import RPi.GPIO as GPIO
import requests
import json 
from twilio.rest import TwilioRestClient  # Twillio Rest Client 



GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# put your own credentials here
ACCOUNT_SID = "AC5ef872f6da5a21de157d80997a64bd33"
AUTH_TOKEN = "[AuthToken]"
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)


def action(pin):
    print 'Sensor detected action!'
    pushMessage("Test message", "*****Alert****** Fire Deteced in Room *****Alert****** ")
    {
        client.messages.create(
                   to="+1XXXXXXXXXX",
                   from_="+1XXXXXXXXXX",
                   body="Test message *****Alert****** Fire Deteced in Room *****Alert****** "",
             )    
    }
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
