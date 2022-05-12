import cv2
import numpy as np

img = cv2.imread("C:\\Users\\C605\\Desktop\\img.jpg")
b, g, r = cv2.split(img)
cv2.imshow("Original image", img)
cv2.imshow("Red", r)
cv2.imshow("Blue", b)
cv2.imshow("Green", g)

diff_green = np.array([0, 130, 0])
image_merge = cv2.merge([r, diff_green, b])
cv2.imshow("different", image_merge)
cv2.waitKey()
