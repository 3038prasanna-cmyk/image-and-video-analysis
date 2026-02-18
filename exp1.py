import cv2
import numpy as np

# Read image
image = cv2.imread('image.jpg')

# Create Gaussian Pyramid
gaussian_pyramid = [image]

for i in range(4):  # 4 levels
    image = cv2.pyrDown(image)
    gaussian_pyramid.append(image)

# Show images
for i, img in enumerate(gaussian_pyramid):
    cv2.imshow(f'Gaussian Level {i}', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
