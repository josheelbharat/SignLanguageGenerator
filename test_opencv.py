# test_opencv.py
import cv2
print("OpenCV Version:", cv2.__version__)
cap = cv2.VideoCapture(0)  # Test webcam
ret, frame = cap.read()
if ret:
    print("Webcam test successful")
else:
    print("Webcam test failed")
cap.release()