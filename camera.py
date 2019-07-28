import numpy as np
import cv2


class Camera:

    def __init__(self, height=224, width=224):

        self.height = height
        self.width = width
        self.capture_width = 3280
        self.capture_height = 2464
        self.fps = 21
        self.value = np.empty((self.height, self.width, 3), dtype=np.uint8)
        self.cap = cv2.VideoCapture("nvarguscamerasrc ! video/x-raw(memory:NVMM), width=(int)1280, height=(int)720,format=(string)NV12, framerate=(fraction)24/1 ! nvvidconv flip-method=2 ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink")
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)


    def capture_frame(self):
        if self.cap.isOpened():
            cv2.namedWindow("demo", cv2.WINDOW_AUTOSIZE)
            while True:
                ret_val, img = self.cap.read();
                cv2.imshow('demo', img)
                cv2.waitKey(10)
        else:
            print("camera open failed")

        cv2.destroyAllWindows()

    def _gst_str(self):
        return 'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=%d, height=%d, format=(string)NV12, framerate=(fraction)%d/1 ! nvvidconv ! video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! videoconvert ! appsink' % (
            self.capture_width, self.capture_height, self.fps, self.width, self.height)






    if __name__ == '__main__':
        capture_frame()