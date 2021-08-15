import numpy as np
import cv2 as cv

cap = cv.VideoCapture(2)
# cap = cv.VideoCapture("/home/user12043/Videos/wait a minute who are you.mp4")
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Add text
    cv.putText(gray, "TEXT", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 2, cv.LINE_AA)
    # Display the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(30) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
