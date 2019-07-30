class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
           gray_face = cv2.resize((gray[y:y + h, x:x + w]), (110, 110))
            eyes = eye_cascade.detectMultiScale(gray_face)
            for (ex, ey, ew, eh) in eyes:
                
                draw_box(gray, x, y, w, h)

        ret, jpeg = cv2.imencode('.jpg', gray)

        return jpeg.tobytes()