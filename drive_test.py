import os
from threading import Thread

import pandas as pd
import pygame
from pygame.locals import *

from camera import Camera
from motor import MotorDriver

# Creating DataFrame and iterator
current_directory = os.getcwd()
training_path = current_directory + "/training/"

print(training_path)

try:
    pd.read_csv(training_path + 'drive_log.csv')
    print("CSV found at {}".format(training_path))
except:
    df = pd.DataFrame(columns=['Index', 'File name', 'Driving direction'])
    print("DataFrame Created")

# Initialize camera
camera = Camera()

# Initialize Pygame and the virtual screen
pygame.init()
windowSurfaceObj = pygame.display.set_mode((640,480),1,16)
FRAMECAPTURE = pygame.USEREVENT + 1
pygame.time.set_timer(FRAMECAPTURE, 500)

# Initialize motor driver
motor = MotorDriver()
motor.allStop()
driving_direction = 0
driving = False
stopping = False

# Start the Pygame loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                motor.forwardDrive()
                driving = True
            elif event.key == K_DOWN:
                motor.reverseDrive()
                stopping = True
            elif event.key == K_RIGHT:
                motor.turnRight()
                driving_direction = 1
            elif event.key == K_LEFT:
                motor.turnLeft()
                driving_direction = -1
            elif event.key == K_s:
                camera.save_csv(df, training_path)
        if event.type == pygame.KEYUP:
            if event.key == K_UP:
                motor.stopDrive()
                driving = False
            elif event.key == K_DOWN:
                motor.stopDrive()
            elif event.key == K_RIGHT:
                motor.goStraight()
                driving_direction = 0
            elif event.key == K_LEFT:
                motor.goStraight()
                driving_direction = 0
        if event.type == FRAMECAPTURE:
            if driving == True :
                th = Thread(target=camera.save_frame, args=[df, driving_direction, training_path])
                th.start()


























