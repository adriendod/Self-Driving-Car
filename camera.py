import numpy as np
import cv2


class Camera:

    def __init__(self, height=224, width=224):

        self.height = height
        self.width = width
        self.value = np.empty((self.height, self.width, 3), dtype=np.uint8)
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)


    def capture_frame(self):
        while (True):
            # Capture frame-by-frame
            ret, frame = cap.read()

            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Display the resulting frame
            cv2.imshow('frame', gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()
