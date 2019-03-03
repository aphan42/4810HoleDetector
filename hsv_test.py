import cv2

def onmouse(k, x, y, s, p):
	global hsv
	if k == 1:
		print(hsv[y,x])

cv2.namedWindow("hsv")
cv2.setMouseCallback("hsv", onmouse)

sample_file = 'data/raw/WIN_20190126_15_00_47_Pro.jpg'
img = cv2.imread(sample_file, 1) # imread_color
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('real', img)
cv2.imshow('hsv', hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()
