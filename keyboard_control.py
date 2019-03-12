import pygame
from pygame.locals import *
import os
import PWM_Config
from time import sleep
from picamera import PiCamera
import config
import pandas as pd
from threading import Thread
import datetime



# Initialize the virtual screen
#os.environ['SDL_VIDEODRIVER'] = 'dummy'
pygame.init()
#pygame.display.set_mode((1,1))
windowSurfaceObj = pygame.display.set_mode((640,480),1,16)

PWM_Config.allStop()
driving_direction = "straight"
driving = False
stopping = False
recording = True

def key_listener():
    while True:
        for event in pygame.event.get():
            # test events, set key states
            if event.type == pygame.KEYDOWN:
                if event.key == K_UP:
                    PWM_Config.forwardDrive()
                    driving = True
                elif event.key == K_DOWN:
                    PWM_Config.reverseDrive()
                    stopping = True
                elif event.key == K_RIGHT:
                    PWM_Config.turnRight()
                    driving_direction = "right"
                elif event.key == K_LEFT:
                    PWM_Config.turnLeft()
                    driving_direction = "left"
                elif event.key == K_s:
                    save_csv(df)
                elif event.key == K_RETURN:
                    recording = False
            if event.type == pygame.KEYUP:
                if event.key == K_UP:
                    PWM_Config.stopDrive()
                elif event.key == K_DOWN:
                    PWM_Config.stopDrive()
                    driving = False
                elif event.key == K_RIGHT:
                    PWM_Config.goStraight()
                    driving_direction = "straight"
                elif event.key == K_LEFT:
                    PWM_Config.goStraight()
                    driving_direction = "straight"

#initializing camera
# camera = PiCamera()
# camera.resolution = (config.width, config.height)
# camera.start_preview()
# sleep(2)

# Saving images and logging driving direction in a data frame

df = pd.DataFrame(columns=['File name', 'Driving direction'])
def data_collection():
    camera = PiCamera()
    camera.resolution = (config.width, config.height)
    camera.start_preview()
    sleep(2)
    df = pd.DataFrame(columns=['File name', 'Driving direction'])
    i = 0
    while recording == True :
        camera.capture(datetime.datetime.now().strftime("%Y-%m-%d-%H.%M.%S.jpg"))
        df.loc[i] = ["capture " + str(i) + ".jpg", driving_direction]
        print("Capture taken")
        i =+ 1
       # elif stopping == True :
        #    break
        #    df.to_csv('drive_log.csv', index=False)
        #    print("File Saved")

def save_csv(df):
    df.to_csv('drive_log.csv', index=False)
    print("File Saved")

t1 = Thread(target = key_listener)
t2 = Thread(target = data_collection)
t1.setDaemon(True)
t2.setDaemon(True)
t1.start()
t2.start()
while True:
    pass















