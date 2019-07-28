import Jetson.GPIO as GPIO
from adafruit_motorkit import MotorKit


class MotorDriver():


kit = MotorKit()

direction = kit.motor4
acceleration = kit.motor2


speed = 0.3

def allStop():
	acceleration.throttle = None
	direction.throttle = None

def forwardDrive():
	acceleration.throttle = -speed

def reverseDrive():
	acceleration.throttle = speed

def stopDrive():
	acceleration.throttle = None

def turnRight():
	direction.throttle = 1

def turnLeft():
	direction.throttle = -1

def goStraight():
	direction.throttle = None

