import cv2
import time
import matplotlib.image as mpimg
import pandas as pd


class Camera:

    def __init__(self, width=1280, height=720):

        self.height = height
        self.width = width
        self.capture_width = 1280
        self.capture_height = 720
        self.fps = 120
        self.cap = cv2.VideoCapture(
            "nvarguscamerasrc ! video/x-raw(memory:NVMM), width=%d, height=%d,format=(string)NV12, "
            "framerate=(fraction)%d/1 ! nvvidconv flip-method=2 ! video/x-raw, width=%d, height=%d, "
            "format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink" % (
            self.capture_width, self.capture_height, self.fps, self.width, self.height))

    def capture_frame(self):
        if self.cap.isOpened():
            ret_val, img = self.cap.read()
            # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            ret, jpeg = cv2.imencode('.jpg', img)
            return jpeg
        else:
            print("camera open failed")
            cv2.destroyAllWindows()
            self.cap.release()

    def save_frame(self, df, driving_direction, training_path):
        try:
            index = df.iloc[-1][0] + 1
        except:
            index = 0

        success, image = self.cap.read()
        if success:
            start = time.time()
            cv2.imwrite(training_path + str(index) + ".jpg", image)
            df.loc[index] = [index, "capture_" + str(index) + ".jpg", driving_direction]
            end = time.time()
            capture_time = end - start
            print("Frame {} Saved in {} mseconds".format(str(index), str(capture_time)))
        else:
            self.cap.release()

    def img_preprocessing(self, img):
        img = mpimg.imread(img)
        img = img[400:720, :, :]
        img = cv2.resize(img, (224, 224))
        img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
        img = cv2.GaussianBlur(img, (3, 3), 0)
        img = img / 255
        img = img.reshape(1, 224, 224, 3)
        return img

    def stop_capture(self):
        cv2.destroyAllWindows()
        self.cap.release()

    def save_csv(self, df, training_path):
        df.to_csv(training_path + 'drive_log.csv', index=False)
        print("File Saved")

