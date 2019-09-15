import Jetson.GPIO as GPIO
from adafruit_motorkit import MotorKit


class MotorDriver:

	def __init__(self):
		self.kit = MotorKit()
		self.leftMotor = self.kit.motor2
		self.rightMotor = self.kit.motor4
		self.leftMotor.throttle = None
		self.rightMotor.throttle = None

	def stopDrive(self):
		self.leftMotor.throttle = None
		self.rightMotor.throttle = None

	def forwardDrive(self, speed=0.75, steering=0):
		if steering < 0 :
			self.leftMotor.throttle = speed
			self.rightMotor.throttle = speed - abs(steering) / 2
		else :
			self.leftMotor.throttle = speed - abs(steering) / 2
			self.rightMotor.throttle = speed