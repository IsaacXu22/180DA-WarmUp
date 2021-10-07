import numpy as np
import cv2 as cv

img = cv.imread('star.jpg', 0)

ret, thresh = cv.threshold(img, 127, 255, 0)

contours, hierarchy = cv.findContours(thresh, 1, 2)

cnt = contours[0]
M = cv.moments(cnt)
print(M)

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

area = cv.contourArea(cnt)
print('The area is: ' + str(area))

perimeter = cv.arcLength(cnt, True)
print('The perimeter is: ' + str(perimeter))

