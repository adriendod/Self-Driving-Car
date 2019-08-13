import Jetson.GPIO as GPIO
from adafruit_motorkit import MotorKit


class MotorDriver:

	def __init__(self):
		self.kit = MotorKit()
		self.leftMotor = self.kit.motor4
		self.rightMotor = self.kit.motor2
		self.leftMotor.throttle = None
		self.rightMotor.throttle = None

	def allStop(self):
		self.acceleration.throttle = None
		self.direction.throttle = None

	def forwardDrive(self, speed=0.5):
		self.leftMotor.throttle = speed
		self.rightMotor.throttle = speed

	def reverseDrive(self, speed=1):
		self.leftMotor.throttle = - speed
		self.rightMotor.throttle = - speed

	def stopDrive(self):
		self.acceleration.throttle = None
		self.direction.throttle = None

	def turnRight(self, turn):
		self.rightMotor.throttle -= turn

	def turnLeft(self, turn):
		self.direction.throttle -= turn

	def goStraight(self):
		self.direction.throttle = None
