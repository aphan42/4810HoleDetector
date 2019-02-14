# this program resizes the raw images, using bicubic interpolation
import os

from PIL import Image

# this function resizes with bicubic Interpolation
def resize_image_set(source='data/raw', destination='data/resize', extension='.jpg'):
		
	raw_files = [i for i in os.listdir(source) \
					if os.path.isfile(os.path.join(source, i))]
	num_resize = len(raw_files)

	# check if resize has already been done
	resized_files = [i for i in os.listdir(destination) \
						if os.path.isfile(os.path.join(destination, i))]

	if len(resized_files) == num_resize:
		print("resize on raw images has already been done at this destination")
	else:
		index = 0

		for file_ in raw_files:
			img = Image.open(os.path.join(raw, file_))
			img_resize = img.resize((64, 64), resample=Image.BICUBIC)
			filepath = "resize" + str(index) + extension
			img_resize.save(os.path.join(resize, filepath))
			index += 1

