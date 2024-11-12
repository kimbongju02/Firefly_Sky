import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'yolov5'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'camera'))

from yolov5 import detect as yolo
from camera import dual_camera as cam

if __name__ == "__main__":
    cam.camera_run()
    #yolo.yolo_run()