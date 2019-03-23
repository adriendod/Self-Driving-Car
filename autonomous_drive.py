import time
import picamera
import picamera.array
import cv2
import PWM_Config
from PIL import Image
import matplotlib.image as mpimg
from keras.models import load_model

#loading model
model = load_model('model.h5')

#setup camera
camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.rotation=180
time.sleep(2)

def capture_yuv():
    camera.capture("stream.jpg", use_video_port = True)
    img = mpimg.imread("stream.jpg")
    img = img[250:480, :,: ]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    img = cv2.GaussianBlur(img, (3,3), 0)
    img = cv2.resize(img, (200,66))
    img = img/255
    img = img.reshape(1,66,200,3)
    return img

def turn_prediction(img):
    prediction = model.predict(img)
    if prediction > 0.3 :
        PWM_Config.turnRight()
        print("Tourne a droite")
    elif prediction < -0.3 :
        PWM_Config.turnLeft()
        print("Tourne a gauche")
    else :
        PWM_Config.goStraight()
        print("Va tout droit")

#Driving
PWM_Config.forwardDrive()

while True :
    start = time.time()
    img = capture_yuv()
    turn_prediction(img)
    end = time.time()
    capture_duration = end - start
    print("Turn took " + str(capture_duration) + " seconds to be predicted.")