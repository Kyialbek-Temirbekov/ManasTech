import cv2
import numpy as np

image = cv2.imread("/home/kyialbek/Projects/python_env/100_0140/DJI_0001.JPG")
if image is None:
	print("Error reading image")
else:
	height, width, _ = image.shape
	grayscale = np.zeros((height, width), np.uint8)
	for h in range(height):
		for w in range(width):
			grayscale[h,w] = int(sum(image[h,w]) / 3)
#	print(grayscale)
#	print(image)
#	print(type(image))
	cv2.imshow("My image", grayscale)
#	print(image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
