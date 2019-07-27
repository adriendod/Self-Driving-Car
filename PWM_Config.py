import Jetson.GPIO as GPIO
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor


mh = Adafruit_MotorHAT()

direction = mh.getMotor(1)
acceleration = mh.getMotor(2)

# set the speed to start, from 0 (off) to 255 (max speed)
direction.setSpeed(150)
acceleration.setSpeed(150)

direction.run(Adafruit_MotorHAT.FORWARD)
# turn on motor
direction.run(Adafruit_MotorHAT.RELEASE)

#///////////////// Define Motor Driver GPIO Pins /////////////////

speed = 0.3

def allStop():
	direction.run(Adafruit_MotorHAT.RELEASE)
	acceleration.run(Adafruit_MotorHAT.RELEASE)

def forwardDrive():
	acceleration.run(Adafruit_MotorHAT.FORWARD)

def reverseDrive():
	acceleration.run(Adafruit_MotorHAT.BACKWARD)

def stopDrive():
	acceleration.run(Adafruit_MotorHAT.RELEASE)	

def turnRight():
	direction.run(Adafruit_MotorHAT.FORWARD)

def turnLeft():
	direction.run(Adafruit_MotorHAT.BACKWARD)

def goStraight():
	direction.run(Adafruit_MotorHAT.RELEASE)

