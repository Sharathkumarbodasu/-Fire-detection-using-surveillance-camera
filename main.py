from ultralytics import YOLO

model = YOLO('yolov8n.pt') 

# Train the model
results = model.train(data='data\data.yaml', epochs=10, imgsz=640)