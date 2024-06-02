# # -*- coding: utf-8 -*-
# Import required packages
import cv2 # real-time image processing (OpenCV) moduleModule that provides the API required for 
import socket # socket programming
import pickle # Module for serialization and de-serialization of objectsData processing module in the format of 
import struct # bytes

# Server IP & Port num
ip = {ip}
port = {port}

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

# Frame size specification
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 480) # Length
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 320) # Width

# Socket object create
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # Connect Server
    client_socket.connect((ip, port))
    
    print("Succes connect")
    
    # Message receive
    while True:
        # Read frame
        retval, frame = capture.read()

        if not retval:
             print('can\'t read frame')
        
        # imencode : image (frame) encoding
        # 1) Output file extension
        # 2) Image to be encoded
        # 3) Encode parameter
        # - For jpg, set the quality of the image (0-100) using cv2.IMWRITE_JPEG_QUALITY
        # - For png, set the compression rate (0 to 9) of the image using cv2.IMWRITE_PNG_COMPRESSION
        # # [return]
        # 1) Encoding result (True/False)
        # 2) Encoded image
        retval, frame = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
        
        # dumps : Serialize data
        # - Serialization: To store data in a line when efficiently stored or sent to a stream
        frame = pickle.dumps(frame)

        print("Send frame size : {} bytes".format(len(frame)))
        
        # sendall : data (frame) transfer
        # - Send all buffer contents of requested data
        # - Call send until all internally transmitted
        # structure.pack : return to byte object
        # ->: Big Endian
        # - Endian: How to arrange multiple consecutive objects in a one-dimensional space, such as a computer's memory
        # - Big endian: Save in order from top byte
        # - L : Unsigned long 4 bits
        client_socket.sendall(struct.pack(">L", len(frame)) + frame)

# Release memory
capture.release()
