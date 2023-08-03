from ultralytics import YOLO
model = YOLO('yolov8n.yaml')
model.train(data="/home/formbay/Desktop/Dataset_od/dataset.yaml",epochs=10)
