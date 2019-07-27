import Jetson.GPIO as GPIO
from adafruit_motorkit import MotorKit

kit = MotorKit()

#direction = kit.getMotor(1)
#acceleration = kit.getMotor(2)


speed = 0.3

def allStop():
	kit.motor2.throttle = None
	kit.motor4.throttle = None

def forwardDrive():
	kit.motor2.throttle = -speed

def reverseDrive():
	kit.motor2.throttle = speed

def stopDrive():
	kit.motor2.throttle = None

def turnRight():
	kit.motor4.throttle = 1

def turnLeft():
	kit.motor4.throttle = -1

def goStraight():
	kit.motor4.throttle = None

