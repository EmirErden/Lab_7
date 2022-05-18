import cv2
import numpy as np
from PIL import Image

img = cv2.imread("C:\\Odev\\New_map.jpg", cv2.IMREAD_COLOR)
r, b, g = cv2.split(img)
cv2.imshow("Original image", img)
cv2.imshow("Red", r)
cv2.imshow("Blue", b)
cv2.imshow("Green", g)

im = Image.open("C:\\Odev\\New_map.jpg").convert("RGB")
R, G, B = im.split()
R = R.point(lambda i: i*0.5)
result = Image.merge("RGB", (R, G, B))
result.show()
cv2.waitKey(0)
