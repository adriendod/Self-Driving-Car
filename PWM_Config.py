import Jetson.GPIO as GPIO
from time import sleep

#///////////////// Define Motor Driver GPIO Pins /////////////////

GPIO.setmode(GPIO.BOARD)

PWM_FORWARD_PIN = 27	
PWM_REVERSE_PIN = 22	

PWM_RIGHT_PIN = 4	
PWM_LEFT_PIN = 17	

# Initialise objects for H-Bridge PWM pins
# Set initial duty cycle to 0 and frequency to 1000
forward = GPIO.PWM(PWM_FORWARD_PIN, 1000)
reverse = GPIO.PWM(PWM_REVERSE_PIN, 1000)
 
right = GPIO.PWM(PWM_RIGHT_PIN, 1000)
left = GPIO.PWM(PWM_LEFT_PIN, 1000)

speed = 0.3

def allStop():
	forward.value = 0
	reverse.value = 0
	right.value = 0
	left.value = 0

def forwardDrive():
	forward.value = speed
	reverse.value = 0

def reverseDrive():
	forward.value = 0
	reverse.value = speed

def stopDrive():
	forward.value = 0
	reverse.value = 0	

def turnRight():
	right.value = 1.0
	left.value = 0

def turnLeft():
	right.value = 0
	left.value = 1.0

def goStraight():
	right.value = 0
	left.value = 0

