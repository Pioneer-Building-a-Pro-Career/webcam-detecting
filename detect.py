from ultralytics import YOLO
import cv2
import time

model = YOLO("yolov8n.pt")  # Load a pretrained YOLOv8 model

# results = model.predict(source="0", stream=True)  # Start webcam detection

# for result in results:
#     frame = result.plot()  # plot() sẽ vẽ bounding box lên frame

#     cv2.imshow("YOLOv8 Webcam", frame)

#     if cv2.waitKey(1) == ord('q'):
#         break

# cv2.destroyAllWindow

# Mở webcam
cap = cv2.VideoCapture(0)  # 0 = webcam mặc định
assert cap.isOpened(), "Không mở được webcam"

# Biến để tính FPS
prev_time = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Không lấy được frame từ webcam!")
        break

    # Dự đoán với YOLO
    results = model.predict(frame, stream=True, verbose=False)

    # Lặp qua từng kết quả trong 1 frame
    for result in results:
        # Vẽ bounding box lên frame
        frame = result.plot()

    # Tính FPS
    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time

    # Hiển thị FPS lên góc trên bên trái
    cv2.putText(
        frame, #img
        f'FPS: {int(fps)}', #text
        (4, 10), #org
        cv2.FONT_HERSHEY_SIMPLEX, #font 
        0.3, #fontScale
        (0, 255, 0), #color
        1) # thickness

    # Hiển thị frame
    cv2.imshow("Real-time Detection", frame)

    # Bấm 'q' để thoát
    if cv2.waitKey(1) == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()