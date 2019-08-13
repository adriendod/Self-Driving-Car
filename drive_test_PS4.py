import os
import pygame
import numpy as np
from pygame.locals import *
from motor_ps4 import MotorDriver
from camera import Camera
import pandas as pd
from threading import Thread


# Creating DataFrame and iterator
current_directory = os.getcwd()
training_path = current_directory + "/training/"

try:
    df = pd.read_csv(training_path + 'drive_log.csv')
    print("CSV found at {}".format(training_path))
except:
    df = pd.DataFrame(columns=['Index', 'File name', 'Driving direction'])
    print("DataFrame Created")


# Initialize camera
camera = Camera()
print("Camera Initialized")


# Initialize Pygame and the virtual screen
pygame.init()
windowSurfaceObj = pygame.display.set_mode((640,480),1,16)
FRAMECAPTURE = pygame.USEREVENT + 1
pygame.time.set_timer(FRAMECAPTURE, 500)


# Get the name of the joystick and print it
pygame.joystick.init()
j = pygame.joystick.Joystick(0)
j.init()
JoyName = pygame.joystick.Joystick(0).get_name()
print("Name of the controller: " + JoyName)


# Initialize motor driver
motor = MotorDriver()
driving_direction = 0
driving = False
stopping = False
speed = 0


# Start the Pygame loop
while True:
    pygame.event.pump()
    steering = j.get_axis(0)
    motor.forwardDrive(speed, steering)
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            if j.get_button(1):
                speed += 0.75
                driving = True
            elif j.get_button(9):
                camera.save_csv(df, training_path)
        if event.type == pygame.JOYBUTTONUP:
            speed += 0.75
            driving = False


        if event.type == FRAMECAPTURE:
            if driving == True :
                th = Thread(target=camera.save_frame, args=[df, steering, training_path])
                th.start()