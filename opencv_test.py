import sys
import cv2

def read_cam():
    cap = cv2.VideoCapture("nvarguscamerasrc ! video/x-raw(memory:NVMM), width=(int)1280, height=(int)720,format=(string)NV12, framerate=(fraction)24/1 ! nvvidconv flip-method=2 ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink")
    if cap.isOpened():
        cv2.namedWindow("demo", cv2.WINDOW_AUTOSIZE)
        while True:
            ret_val, img = cap.read()
            #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            ret, img = cv2.imencode('.jpg', img)
            cv2.imshow('demo',img)
            cv2.waitKey(10)
    else:
     print("camera open failed")

    cv2.destroyAllWindows()


if __name__ == '__main__':
    read_cam()