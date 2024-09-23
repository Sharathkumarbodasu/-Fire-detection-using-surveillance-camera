import cv2
from ultralytics import YOLO

model = YOLO('weights/fire_detection.pt')  

cap = cv2.VideoCapture("videoplayback.mp4") 


while True:
  
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture image.")
        break

    # Perform inference on the frame
    results = model(frame)
   

    # Print detailed results
    
    annotated_frame = results[0].plot()
    # Display the resulting frame
    cv2.imshow('YOLOv8 Webcam Inference', annotated_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):

        break

# When everything is done, release the capture and close the windows
cap.release()
cv2.destroyAllWindows()
