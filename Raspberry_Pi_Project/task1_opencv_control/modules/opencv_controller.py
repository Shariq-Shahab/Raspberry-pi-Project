import logging
import threading
import cv2
import numpy as np
USE_FAKE_PI_CAMERA = True # Chage to FALSE if testing in the Raspberry Pi

if USE_FAKE_PI_CAMERA:
    from .camera import Camera  # For running app
else:
    from .pi_camera import Camera  # For running Raspberry Pi

log = logging.getLogger(
    __name__)  # Creates a logger instance, we use it to log things out


class OpenCVController(object):

    def __init__(self):
        self.current_color = [False, False, False, False]
        self.camera = Camera()
        print('OpenCV controller initiated')

    def process_frame(self):  # generate frame by frame from camera
        while True:
            # Capture frame-by-frame
            frame = self.camera.get_frame()  # read the camera frame

            ###Process frame here

            hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            colors = {
                'Blue': ([92, 64, 80], [108, 255, 255]),
                'Purple': ([120, 50, 80], [155, 255, 255]),
                'Yellow': ([25, 150, 170], [35, 255, 255]),
                'Green': ([40, 50, 80], [60, 255, 255])
            }

            for i, (color, (lower, upper)) in enumerate(colors.items()):
                mask = cv2.inRange(hsv_frame, np.array(lower), np.array(upper))
                contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                for contour in contours:
                    area = cv2.contourArea(contour)
                    if area > 200:
                       x, y, w, h = cv2.boundingRect(contour)
                       cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 8)
                       cv2.putText(frame, color, (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
            
            # Code for red mark detection
            color_2 = {'Red Mark': ([156,50,84],[190,255,255])}
            for color, (lower, upper) in color_2.items():
                if color == 'Red Mark':
                    mask =cv2.inRange(hsv_frame, np.array(lower), np.array(upper))
                    contours, _=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                    for contour in contours:
                        area =cv2.contourArea(contour)
                        if area > 100:
                            x, y, w, h = cv2.boundingRect(contour)
                            cv2.rectangle(frame, (x, y), (x + w, h + w), (0, 0, 255), 8)
                            cv2.putText(frame, color, (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

                            self.red_mark_position = (x,y)
                            if self.red_mark_position > (532, 200):
                                self.current_color = [False, False, False, True]
                            elif self.red_mark_position > (422, 194):
                                self.current_color = [False, False, True, True]
                            elif self.red_mark_position > (352, 187):
                                self.current_color = [False, False, True, False]
                            elif self.red_mark_position > (270, 180):
                                self.current_color = [False, True, True, False]
                            elif self.red_mark_position > (287, 188):
                                self.current_color = [False, True, False, False]
                            elif self.red_mark_position > (118, 187):
                                self.current_color = [True, True, False, False]
                            elif self.red_mark_position > (83, 186):
                                self.current_color = [True, False, False, False]
                                break
                            
            return frame


    def get_current_color(self):
        return self.current_color
