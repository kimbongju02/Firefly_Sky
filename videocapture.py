import cv2
import time
from detect import detect
import time

def gstreamer_pipeline(
    sensor_id=0,
    capture_width=480,
    capture_height=320,
    display_width=480,
    display_height=320,
    framerate=30,
    flip_method=0,
):
    return (
        "nvarguscamerasrc sensor-id=%d ! "
        "video/x-raw(memory:NVMM), width=(int)%d, height=(int)%d, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            sensor_id,
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )

capture = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)

try:
    while True:
        retval, frame = capture.read()

        if not retval:
                print('can\'t read frame')
        
        cv2.imwrite(filename, frame)
        detect()
        
        time.sleep(5)
finally:
    capture.release()