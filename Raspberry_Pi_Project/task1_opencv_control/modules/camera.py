# Please note that this is a fake camera, it will just
# yield the images 1.jpg, 2.jpg, 3.jg and 4.jpg. It is
# just for testing purposes. You should actually use the
# picamera module and implement the get_frame properly

from time import time
from time import sleep
import os, sys
import cv2


class Camera(object):
    def __init__(self):
        directory = os.path.join(os.path.dirname(__file__), 'test_frames')
        self.test_frames_name = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg']
        self.frames = [cv2.imread(os.path.join(directory, f))
        for f in self.test_frames_name]
        self.current_frame = int(time()) % 7
        self.count = 0

    def get_frame(self):
        if (self.count > 1):
            self.current_frame = int(time()) % 7
            self.count = 0
        index = int(time()) % 7
        print('Frame', self.test_frames_name[self.current_frame])
        self.count = self.count + 1
        return self.frames[self.current_frame]
