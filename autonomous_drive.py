import time
from keras.models import load_model
from camera import Camera
from old.motor import MotorDriver
import cv2

#loading model
model = load_model('model.h5')

# Initialize camera and motor
camera = Camera()
motor = MotorDriver()
print("Camera Initialized")
time.sleep(2)

def turn_prediction(img):
    prediction = model.predict(img)
    MotorDriver.forwardDrive(0.75, prediction)

while True :
    start = time.time()
    img = camera.capture_frame()
    cv2.imwrite("stream.jpg", img)
    img = camera.img_preprocessing("stream.jpg")
    turn_prediction(img)
    end = time.time()
    capture_duration = end - start
    print("Turn took " + str(capture_duration) + " seconds to be predicted.")