from ultralytics import YOLO
# from ultralytics.yolo.v8.detect.predict import DetectionPredictor

import cv2

model = YOLO("C:/Users/david/PycharmProjects/Lineas_metro/runs/detect/train5/weights/best.pt")

results = model.predict(source='0', show=True)
print(results)