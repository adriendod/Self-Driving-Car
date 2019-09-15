import Jetson.GPIO as GPIO
from adafruit_motorkit import MotorKit


class MotorDriver:

	def __init__(self):
		self.kit = MotorKit()
		self.direction = self.kit.motor4
		self.acceleration = self.kit.motor2

	def allStop(self):
		self.acceleration.throttle = None
		self.direction.throttle = None

	def forwardDrive(self, speed=1):
		self.acceleration.throttle = -speed

	def reverseDrive(self, speed=1):
		self.acceleration.throttle = speed

	def stopDrive(self):
		self.acceleration.throttle = None

	def turnRight(self):
		self.direction.throttle = 1

	def turnLeft(self):
		self.direction.throttle = -1

	def goStraight(self):
		self.direction.throttle = None
