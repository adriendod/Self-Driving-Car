import time
import picamera
import picamera.array
import cv2
import PWM_Config
from PIL import Image
import matplotlib.image as mpimg
from keras.models import load_model

model = load_model('model.h5')
#setup camera
camera = picamera.PiCamera()
camera.resolution = (360, 640)
time.sleep(2)

def capture_yuv():
	# #capturing in YUV
 #    start = time.time()
 #    output = picamera.array.PiYUVArray(camera)
 #    camera.capture(output, 'yuv')
 #    print('Captured %dx%d image' % (output.array.shape[1], output.array.shape[0]))
 #    end = time.time()
 #    capture_duration = end - start
 #    print("Capture took " + str(capture_duration) + " seconds.")
    start = time.time()
    camera.capture("stream.jpg")
    end = time.time()
    capture_duration = end - start
    print(capture_duration)

    #processing
    start = time.time()
    img = mpimg.imread("stream.jpg")
    img = img[250:480, :,: ]
    img = cv2.GaussianBlur(img, (3,3), 0)
    img = cv2.resize(img, (200,66))
    img = img/255
    img = img.reshape(1,66,200,3)
    end = time.time()
    capture_duration = end - start
    print("Image took " + str(capture_duration) + " seconds to preprocess.")

    #predicting
    if model.predict(image) > 0.3 :
        PWM_Config.turnRight()
        print("Tourne a droite")
    elif model.predict(image) < -0.3 :
        PWM_Config.turnLeft()
        print("Tourne a gauche")
    else :
        PWM_Config.goStraight()
        print("Va tout droit")




#Driving
PWM_Config.forwardDrive()

while True :
    capture_yuv()
    start = time.time()
    end = time.time()
    capture_duration = end - start
    print("Turn took " + str(capture_duration) + " seconds to be predicted.")