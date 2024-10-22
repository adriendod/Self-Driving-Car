import pygame
from pygame.locals import *
import time
from picamera import PiCamera
from old import config, motor
import pandas as pd
from threading import Thread



# Initialize Pygame and the virtual screen
#os.environ['SDL_VIDEODRIVER'] = 'dummy'
pygame.init()
#pygame.display.set_mode((1,1))
windowSurfaceObj = pygame.display.set_mode((640,480),1,16)
FRAMECAPTURE = pygame.USEREVENT + 1
pygame.time.set_timer(FRAMECAPTURE, 1000)

#PWM Setup
PWM_Config.allStop()
driving_direction = "straight"
driving = False
stopping = False


#Camera setup
camera = PiCamera()
camera.resolution = (config.width, config.height)
#camera.shutter_speed = 100000
camera.rotation=180
#camera.iso = 800
camera.start_preview()
time.sleep(2)


# Creating DataFrame and iterator
df = pd.DataFrame(columns=['File name', 'Driving direction'])
i = 1

def save_csv(dataframe):
    dataframe.to_csv('drive_log.csv', index=False)
    print("File Saved")

def capture_frame():
    if driving == True :
        global i
        start = time.time()
        camera.capture("capture " + str(i) + ".jpg")
        df.loc[i] = ["capture " + str(i) + ".jpg", driving_direction]
        print("Capture taken:", i)
        i += 1 
        end = time.time()
        capture_duration = end - start
        print(capture_duration)



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
                save_csv(df)
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
                th = Thread(target=capture_frame)
                th.start()

























