# Fire Detection Drone Project
드론과 객체인식을 사용하여 산불 및 연기 감지

### 사용 부품
Pixhawk2.4.8
  - 수신기
  - Radiolink M8N M10N SE100 : GPS
  - Safe switch
  - Buzzer
Jetson nano Develop kit-B01
RPI 8MP CAMERA BOARD : 일반 카메라
RPI NOIR CAMERA BOARD : 적외선 카메라
Lipo Battery
  - 3S 5000mah
T2212-920KV Brushless DC electric motor

### 설계
1. 드론은 지정된 경로를 자동으로 비행한다.
2. 드론이 비행하는 동안 Jetson nano는 카메라를 통해 비디오 촬영
3. 비디오 영상을 5초 단위로 저장하여 YOLOv5에서 객체 인식
