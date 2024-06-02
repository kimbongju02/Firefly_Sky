# MIT License
# Copyright (c) 2019 JetsonHacks
# See license
# Using a CSI camera (such as the Raspberry Pi Version 2) connected to a
# NVIDIA Jetson Nano Developer Kit using OpenCV
# Drivers for the camera and OpenCV are included in the base image
 
import cv2
 
# gstreamer_pipeline returns a GStreamer pipeline for capturing from the CSI camera
# Defaults to 1280x720 @ 60fps
# Flip the image by setting the flip_method (most common values: 0 and 2)
# display_width and display_height determine the size of the window on the screen
 
 
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

 
 
def show_camera():
    # To flip the image, modify the flip_method parameter (0 and 2 are the most common)
    print("------------print gstreamer_pipeline(flip_method=0)------------ \n", gstreamer_pipeline(flip_method=0))
    cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)
    
    if cap.isOpened():
        
        # Window
        while True:
            ret_val, img = cap.read()
            if ret_val == 0:
                print("fail to read frame")
            cv2.imshow("CSI Camera", img)

        cap.release()
        cv2.destroyAllWindows()
    else:
        print("------------------------Unable to open camera---------------------------")
 
 
if __name__ == "__main__":
    show_camera()
