from PIL import Image
import matplotlib.image as mpimg
from keras.models import load_model
import time


#loading model
model = load_model('model.h5')

time.sleep(2)

def capture_yuv():
    img = mpimg.imread("image.jpg")
    img = img[250:480, :,: ]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    img = cv2.GaussianBlur(img, (3,3), 0)
    img = cv2.resize(img, (200,66))
    img = img/255
    img = img.reshape(1,66,200,3)
    return img

def turn_prediction(img):
    prediction = model.predict(img)

start = time.time()
img = capture_yuv()
turn_prediction(img)
end = time.time()
capture_duration = end - start
print("Turn took " + str(capture_duration) + " seconds to be predicted.")