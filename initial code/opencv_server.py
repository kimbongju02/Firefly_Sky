# import package
import socket # socket programming API
import struct # Data processing module in byte format
import pickle # Module for serialization and de-serialization of objects
import cv2 # OpenCV module

# server ip & port num
ip = {ip}
port = {port}

# socket object
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# socket address
server_socket.bind((ip, port))
print('socket bind success')

# connect listening
server_socket.listen(10) 
print('socket listening')

print('Waiting for Client Connection')

# connect acces
client_socket, address = server_socket.accept()
print('client ip address :', address[0])

# Buffer to place received data (byte object)
data_buffer = b""

# calcsize : data size(byte)
# - L : unsigned long integer(unsigned long) 4 bytes
data_size = struct.calcsize("L")

while True:
    # The size of the data stored in the buffer is smaller than the size of the data you set
    while len(data_buffer) < data_size:
        # Receiving data
        data_buffer += client_socket.recv(4096)

    # Split the stored data in the buffer
    packed_data_size = data_buffer[:data_size]
    data_buffer = data_buffer[data_size:] 
    
    # structure.unpack : return converted byte object to original data
    # ->: Big Endian
    # - Endian: How to arrange multiple consecutive objects in a one-dimensional space, such as a computer's memory
    # - Big endian: Save in order from top byte
    # - L : Unsigned long 4 bits
    frame_size = struct.unpack(">L", packed_data_size)[0]
    
    # The size of the data stored in the buffer is smaller than the size of the frame data
    while len(data_buffer) < frame_size:  
        # Receiving data
        data_buffer += client_socket.recv(4096)
    
    # split data frame
    frame_data = data_buffer[:frame_size]
    data_buffer = data_buffer[frame_size:]
    
    print("receive frame data : {} bytes".format(frame_size))
    
    # loads : Inverse serialization of serialized data
    # - de-serialization: Restoring serialized files or byte objects to their original data
    frame = pickle.loads(frame_data)
    
    # imdecode : image (frame) decoding
   # 1) Array of encoded images
   # 2) Options for reading image files
   # - IMREAD_COLOR: Read image as COLOR
    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
    
    # print frame
    cv2.imshow('Frame', frame)
    
    # input 'q' quit 
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close socket
client_socket.close()
server_socket.close()
print('connect close')
   
# all window close
cv2.destroyAllWindows()
