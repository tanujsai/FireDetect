
#encoding=utf-8

# the sensor has to be connected to pin 1 for power, pin 6 for ground
# and pin 7 for signal(board numbering!).

# Pushetta Notification System 


import time
import sys
import RPi.GPIO as GPIO
import urllib2
import json

def sendNotification(token, channel, message):
	data = {
		"body" : message,
		"message_type" : "text/plain"
	}
    
req = urllib2.Request('http://api.pushetta.com/api/pushes/{0}/'.format(channel))
req.add_header('Content-Type', 'application/json')
req.add_header('Authorization', 'Token {0}'.format(token))
response = urllib2.urlopen(req, json.dumps(data))
	
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def action(pin):
    sendNotification("#API_CODE", "Fire", "Hello")   #API_CODE From pushetta
    print 'Sensor detected action!'
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
