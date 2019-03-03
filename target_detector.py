import os
import cv2
import numpy as np

path_to_raw_images = 'data/resize/'
path_to_processed_images = 'data/processed/'
raw_image_filenames = os.listdir(path_to_raw_images)

image_no = 0
for filename in raw_image_filenames:
	full_path = path_to_raw_images + filename
	img = cv2.imread(full_path)
	if img is not None:
		imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
		ret, thresh = cv2.threshold(imgray, 66, 255, cv2.THRESH_BINARY)
		contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, \
						       cv2.CHAIN_APPROX_SIMPLE)
		filtered_contours = []
		for contour in contours:
			if cv2.contourArea(contour) < 1e4:
				filtered_contours.append(contour)
		contour_points = []
		for contour in filtered_contours:
			for point in contour:
				contour_points.append(point[0])
		contour_points = np.array(contour_points)
		min_vals = np.amin(contour_points, axis=0)
		max_vals = np.amax(contour_points, axis=0)
		cv2.drawContours(img, filtered_contours, -1, (0, 255, 0), 2)
		cv2.rectangle(img, (min_vals[0], min_vals[1]), \
			     (max_vals[0], max_vals[1]), (255, 255, 0), 2)
		cv2.imwrite(path_to_processed_images + 'processed' + str(image_no) \
			    + '.png', img)
		image_no += 1
	else:
		print("error reading image")
		break
