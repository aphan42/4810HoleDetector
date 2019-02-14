# this program resizes the raw images, using bicubic interpolation

import os

from PIL import Image

raw = 'data/raw'
resize = 'data/resize'

raw_files = [i for i in os.listdir(raw) if os.path.isfile(os.path.join(raw, i))]
index = 0
extension = ".jpg"

for file_ in raw_files:
	img = Image.open(os.path.join(raw, file_))
	img_resize = img.resize((64, 64), resample=Image.BICUBIC)
	filepath = "resize" + str(index) + extension
	img_resize.save(os.path.join(resize, filepath))
	index += 1
