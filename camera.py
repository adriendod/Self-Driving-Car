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
        self.cap = cv2.VideoCapture(self._gst_str(), cv2.CAP_GSTREAMER)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)


    def capture_frame(self):
        while (True):
            # Capture frame-by-frame
            ret, frame = self.cap.read()
            print("frame")
            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Display the resulting frame
            cv2.imshow('frame', gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # When everything done, release the capture
        self.cap.release()
        cv2.destroyAllWindows()

    def _gst_str(self):
        return 'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=%d, height=%d, format=(string)NV12, framerate=(fraction)%d/1 ! nvvidconv ! video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! videoconvert ! appsink' % (
            self.capture_width, self.capture_height, self.fps, self.width, self.height)
