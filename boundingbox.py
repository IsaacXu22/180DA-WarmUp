import numpy as np
import cv2 as cv
import matplotlib as plt

cap = cv.VideoCapture(0)

while(True):

    ret, frame = cap.read()
    thresh = cv.inRange(frame, (80, 0, 0), (255, 75, 75))
    
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    cnt = contours[1]
    x,y,w,h = cv.boundingRect(cnt)
    cv.rectangle(frame, (x,y),(x+w, y+h), (0, 255, 0),5)
    cv.imshow('Modified B/W', thresh)
    cv.imshow('Original', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows