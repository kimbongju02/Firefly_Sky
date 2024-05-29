from roboflow import Roboflow
import cv2
import os

# Roboflow API 키 사용
rf = Roboflow(api_key="GLJ67cnyAjcKdrneCY3l")
project = rf.workspace().project("mugs-uyv4e")
model = project.version(1).model

# 절대 경로 사용
image_path = '/home/young/Desktop/coding/tt.jpg'
output_path = '/home/young/Desktop/coding/output.jpg'

# Roboflow 모델 예측
result = model.predict(image_path, confidence=40, overlap=30).json()

# 예측 결과에서 라벨 추출
labels = [item["class"] for item in result["predictions"]]

# 이미지 불러오기
if not os.path.exists(image_path):
    print(f"Error: The file at {image_path} does not exist.")
else:
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to read the image at {image_path}")
    else:
        # 예측 결과를 이미지에 주석으로 추가하고 중심 좌표 출력
        with open('/home/young/Desktop/coding/coordinates.txt', 'w') as f:
            for prediction in result["predictions"]:
                x_center, y_center = prediction["x"], prediction["y"]
                class_name = prediction["class"]
                f.write(f"Object: {class_name}, Center Coordinates: ({x_center}, {y_center})\n")

                # 예측된 객체 주위에 사각형 그리기
                width, height = prediction["width"], prediction["height"]
                x0 = int(x_center - width / 2)
                y0 = int(y_center - height / 2)
                x1 = int(x_center + width / 2)
                y1 = int(y_center + height / 2)
                mid_x = int(abs(abs(x0) + abs(x1))/2)
                mid_y = int(abs(abs(y0) + abs(y1))/2)
                cv2.rectangle(image, (x0, y0), (x1, y1), (0, 255, 0), 2)
                cv2.circle(image, (mid_x, mid_y), 20, (255, 255, 0))
                # cv2.circle(image, (x_center, y_center), 10, (0,0,0))

        # 주석이 추가된 이미지 저장
        cv2.imwrite(output_path, image)
        print(f"Annotated image saved to {output_path}")
        print(f"Object coordinates saved to /home/young/Desktop/coding/coordinates.txt")
