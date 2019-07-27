from gpiozero import PWMOutputDevice

leftWheels = PWMOutputDevice(21)
leftWheels.frequency = 1000
leftWheels.value = 0.50

#///////////////// Define Motor Driver GPIO Pins /////////////////

PWM_FORWARD_PIN = 27	
PWM_REVERSE_PIN = 22	

PWM_RIGHT_PIN = 4	
PWM_LEFT_PIN = 17	

# Initialise objects for H-Bridge PWM pins
# Set initial duty cycle to 0 and frequency to 1000
forward = PWMOutputDevice(PWM_FORWARD_PIN, True, 0, 1000)
reverse = PWMOutputDevice(PWM_REVERSE_PIN, True, 0, 1000)
 
right = PWMOutputDevice(PWM_RIGHT_PIN, True, 0, 1000)
left = PWMOutputDevice(PWM_LEFT_PIN, True, 0, 1000)

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

