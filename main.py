import cv2 
import numpy as np

#load image
image = cv2.imread('datasets\dog.jpg')

#convert to gray
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#invert color
inverted_image = cv2.bitwise_not(gray_image)

#invert image
blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), 0) 
pencil_sketch = cv2.divide(gray_image, 255 - blurred_image, scale=256.0)

#show image
cv2.imshow('Original Image', image) 
cv2.imshow('Pencil Sketch', pencil_sketch) 
cv2.waitKey(0) 
cv2.destroyAllWindows()