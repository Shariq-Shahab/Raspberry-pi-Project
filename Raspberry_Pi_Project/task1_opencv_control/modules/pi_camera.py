import cv2
class Camera(object):
    def __init__(self):
        self.camera = cv2.VideoCapture(0)
        print("Starting pi camera")

    def get_frame(self):
        success, frame = self.camera.read()
        if not success:
            print("not")
        else:
            return frame
