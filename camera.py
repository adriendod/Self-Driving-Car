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
            ret_val, img = self.cap.read()
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            ret, jpeg = cv2.imencode('.jpg', img)
            return jpeg
        else:
            print("camera open failed")
            cv2.destroyAllWindows()
            cap.release()

    def save_frame(self, path_output_dir):
        global count
        success, image = cap.read()
        if success:
            cv2.imwrite(os.path.join(path_output_dir, '%d.jpg') % count, image)
            df.loc[i] = ["capture " + str(i) + ".jpg", driving_direction]
            count += 1
            print("Frame Captured and Saved")
        else:
            break
        cap.release()

    def stop_capture(self):
        cv2.destroyAllWindows()
        cap.release()

    def _gst_str(self):
        return 'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=%d, height=%d, format=(string)NV12, framerate=(fraction)%d/1 ! nvvidconv ! video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! videoconvert ! appsink' % (
            self.capture_width, self.capture_height, self.fps, self.width, self.height)
