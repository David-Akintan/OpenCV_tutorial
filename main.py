# import the necessary modules

import cv2 as cv
import sys 

image = cv.imread('assets/12.jpeg', 1)   # reads the image 
# Check if the image loaded successfully
if image is None:
    sys.exit('Error while loading image')

image = cv.resize(image, (0, 0), fx=0.5, fy=0.5)  # resize the image (Half its original)
image = cv.rotate(image, cv.cv2.ROTATE_90_CLOCKWISE)  # rotate the image

cv.imshow("Display Window", image)  # Displays image on a new window
cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite('assets/new_img.jpg', image)   # Writes the processed image to a new file