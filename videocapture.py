import cv2
import time
from detect import detect

def gstreamer_pipeline(
    sensor_mode=0,
    capture_width=480,
    capture_height=320,
    display_width=480,
    display_height=320,
    framerate=30,
    flip_method=0,
):
    return (
        "gst-launch-1.0 nvarguscamerasrc sensor_mode=%d ! "
        "\'video/x-raw(memory:NVMM),width=%d,height=%d,framerate=%d/1\' ! "
        "nvvidconv flip-method=%d ! "
        "\'video/x-raw,width=%d,height=%d\' ! "
        "videoconvert ! "
        "video/x-raw, format=NV12 ! appsink"
        % (
            sensor_mode,
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )
print("------------print gstreamer_pipeline(flip_method=0)------------ \n", gstreamer_pipeline(flip_method=0))

capture = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 480) # Length
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 320) # Width

try:
    while True:
        retval, frame = capture.read()

        if not retval:
                print('can\'t read frame')
        
        #cv2.imwrite(filename, frame)
        #detect()
        
        time.sleep(5)
finally:
    capture.release()