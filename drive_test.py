import pygame
import numpy as np
from pygame.locals import *
from motor import MotorDriver
from camera import Camera
import pandas as pd
from threading import Thread

#camera
camera = Camera()
motor = MotorDriver()

# Initialize Pygame and the virtual screen
pygame.init()
windowSurfaceObj = pygame.display.set_mode((640,480),1,16)
FRAMECAPTURE = pygame.USEREVENT + 1
pygame.time.set_timer(FRAMECAPTURE, 1000)

#PWM Setup
motor.allStop()
driving_direction = "straight"
driving = False
stopping = False

# Creating DataFrame and iterator
df = pd.DataFrame(columns=['File name', 'Driving direction'])
count = 1



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
                print("save csv (not implemented)")
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
            print("frame capture")
            th = Thread(target=camera.save_frame, args=[df, driving_direction, "/"])
            th.start()


























