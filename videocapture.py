import numpy as np
import cv2 as cv


#What this does is capture a video in black and white
cap = cv.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv.imshow('frame',gray)
    
    #pretty sure this is the button to close the thing
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

#When everything is done, release the capture
cap.release()
cv.destroyAllWindows()

