import cv2
import numpy as np

import os

raw = "data/raw"
raw_files = os.listdir(raw)
filtered = "data/filtered"

# thresholds in hsv values
lower_green = np.array([0, 0, 118])
upper_green = np.array([255, 255, 255])

image_no = 0

for file_ in raw_files:
	img = cv2.imread(os.path.join(raw, file_), 1)
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, lower_green, upper_green)
	res = cv2.bitwise_and(img, img, mask=mask)
	cv2.imwrite(filtered + '/filtered' + str(image_no) + '.png', res)
	# cv2.imshow('realimg', img)
	# cv2.imshow('mask' , res)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()


