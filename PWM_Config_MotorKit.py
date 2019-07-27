import Jetson.GPIO as GPIO
from adafruit_motorkit import MotorKit

kit = MotorKit(i2c=0)

direction = mh.getMotor(1)
acceleration = mh.getMotor(2)


speed = 0.3

def allStop():
	kit.motor1.throttle = None
	kit.motor2.throttle = None

def forwardDrive():
	kit.motor1.throttle = speed

def reverseDrive():
	kit.motor1.throttle = -speed

def stopDrive():
	kit.motor1.throttle = None

def turnRight():
	kit.motor2.throttle = 1

def turnLeft():
	kit.motor2.throttle = -1

def goStraight():
	kit.motor2.throttle = None

