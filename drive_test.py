import pygame
import numpy as np
from pygame.locals import *
from motor import MotorDriver
import pandas as pd
import cv2

#camera
camera = cv2.VideoCapture("nvarguscamerasrc ! video/x-raw(memory:NVMM), width=(int)1280, height=(int)720,format=(string)NV12, framerate=(fraction)24/1 ! nvvidconv flip-method=2 ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink")




motor = MotorDriver()

# Initialize Pygame and the virtual screen
#os.environ['SDL_VIDEODRIVER'] = 'dummy'
pygame.init()
#pygame.display.set_mode((1,1))
windowSurfaceObj = pygame.display.set_mode((640,480),1,16)
FRAMECAPTURE = pygame.USEREVENT + 1
pygame.time.set_timer(FRAMECAPTURE, 1000)

#PWM Setup
motor.allStop()
driving_direction = "straight"
driving = False
stopping = False

'''
#Camera setup
camera = PiCamera()
camera.resolution = (config.width, config.height)
#camera.shutter_speed = 100000
camera.rotation=180
#camera.iso = 800
camera.start_preview()
time.sleep(2)
'''

# Creating DataFrame and iterator
df = pd.DataFrame(columns=['File name', 'Driving direction'])
i = 1



while True:
    ret, frame = camera.read()
    windowSurfaceObj.fill([0, 0, 0])
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = np.rot90(frame)
    frame = pygame.surfarray.make_surface(frame)
    screen.blit(frame, (0, 0))
    pygame.display.update()

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


























