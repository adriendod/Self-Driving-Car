import pygame
from pygame.locals import *
import PWM_Config_MotorKit
import config
import pandas as pd




# Initialize Pygame and the virtual screen
#os.environ['SDL_VIDEODRIVER'] = 'dummy'
pygame.init()
#pygame.display.set_mode((1,1))
windowSurfaceObj = pygame.display.set_mode((640,480),1,16)
FRAMECAPTURE = pygame.USEREVENT + 1
pygame.time.set_timer(FRAMECAPTURE, 1000)

#PWM Setup
PWM_Config_MotorKit.allStop()
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
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                PWM_Config_MotorKit.forwardDrive()
                driving = True
            elif event.key == K_DOWN:
                PWM_Config_MotorKit.reverseDrive()
                stopping = True
            elif event.key == K_RIGHT:
                PWM_Config_MotorKit.turnRight()
                driving_direction = 1
            elif event.key == K_LEFT:
                PWM_Config_MotorKit.turnLeft()
                driving_direction = -1
            elif event.key == K_s:
                print("save csv (not implemented)")
        if event.type == pygame.KEYUP:
            if event.key == K_UP:
                PWM_Config_MotorKit.stopDrive()
                driving = False
            elif event.key == K_DOWN:
                PWM_Config_MotorKit.stopDrive()
            elif event.key == K_RIGHT:
                PWM_Config_MotorKit.goStraight()
                driving_direction = 0
            elif event.key == K_LEFT:
                PWM_Config_MotorKit.goStraight()
                driving_direction = 0
        if event.type == FRAMECAPTURE:
            print("frame capture")


























