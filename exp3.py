import cv2
import numpy as np

# ------------------------
# Helper Functions
# ------------------------
def translate(image, tx, ty):
    M = np.float32([[1, 0, tx], [0, 1, ty]])
    return cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

def rotate(image, angle, scale=1.0):
    h, w = image.shape[:2]
    center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    return cv2.warpAffine(image, M, (w, h))

def scale_image(image, fx, fy):
    return cv2.resize(image, None, fx=fx, fy=fy)

def shear(image, shx=0.0, shy=0.0):
    rows, cols = image.shape[:2]
    M = np.float32([[1, shx, 0],
                    [shy, 1, 0]])
    return cv2.warpAffine(image, M, (cols + int(rows*shx), rows + int(cols*shy)))

def affine_transform(image):
    rows, cols = image.shape[:2]
    pts1 = np.float32([[50,50],[200,50],[50,200]])
    pts2 = np.float32([[10,100],[200,50],[100,250]])
    M = cv2.getAffineTransform(pts1, pts2)
    return cv2.warpAffine(image, M, (cols, rows))

def perspective_transform(image):
    rows, cols = image.shape[:2]
    pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
    pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
    M = cv2.getPerspectiveTransform(pts1, pts2)
    return cv2.warpPerspective(image, M, (300,300))

# ------------------------
# Main Program
# ------------------------
image = cv2.imread('image.jpg')
if image is None:
    print("Image not found!")
    exit()

# Resize to fit screen
image = cv2.resize(image, (400, 400))

cv2.namedWindow('Original')
cv2.imshow('Original', image)

# Example: Apply all transforms one by one
translated = translate(image, tx=50, ty=100)
rotated = rotate(image, angle=45)
scaled = scale_image(image, fx=1.5, fy=1.5)
sheared = shear(image, shx=0.5)
affined = affine_transform(image)
perspect = perspective_transform(image)

# Display results
cv2.imshow('Translated', translated)
cv2.imshow('Rotated', rotated)
cv2.imshow('Scaled', scaled)
cv2.imshow('Sheared', sheared)
cv2.imshow('Affine', affined)
cv2.imshow('Perspective', perspect)

cv2.waitKey(0)
cv2.destroyAllWindows()
