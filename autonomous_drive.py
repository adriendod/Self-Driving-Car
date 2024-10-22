import time
from keras.models import load_model
from camera import Camera
from motor import MotorDriver
import cv2

#loading model
model = load_model('model.h5')

# Initialize camera and motor
camera = Camera()
motor = MotorDriver()
print("Camera Initialized")
time.sleep(2)

def turn_prediction(img):
    prediction = min(1, max(-1,model.predict(img) * 1.5))
    print(prediction)
    motor.forwardDrive(0.75, prediction)

while True :
    start = time.time()
    img = camera.capture_frame()
    img = camera.img_preprocessing(img)
    turn_prediction(img)
    end = time.time()
    capture_duration = end - start