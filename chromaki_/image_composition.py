import numpy as np
import cv2
import math

#portrait

filename = 'chroma_green.jpeg'
# 画像の読み込み
image1 = cv2.imread(filename)

# 画像の幅，高さ，bpp（チャンネル数）を取得
width1 = image1.shape[1]
height1 = image1.shape[0]
bpp1 = image1.shape[2] * image.dtype.type(0).nbytes
imagesize1 = image1.nbytes



#background

filename = 'green.jpeg'
# 画像の読み込み
image2 = cv2.imread(filename)
# 画像の幅，高さ，bpp（チャンネル数）を取得
width2 = image2.shape[1]
height2 = image2.shape[0]
bpp2 = image2.shape[2] * image.dtype.type(0).nbytes
imagesize2 = image1.nbytes


image_synthesis = np.zeros([height, width, bpp], dtype=np.uint8)


for y in range(height):
  for x in range(width):
    image_synthesis[y, x, 0] = (image1[y, x, 0] + image2[y, x, 0]) / 2
    image_synthesis[y, x, 1] = (image1[y, x, 1] + image2[y, x, 1]) / 2
    image_synthesis[y, x, 2] = (image1[y, x, 2] + image2[y, x, 2]) / 2


# 画像の保存
cv2.imwrite('result2-1.jpg', image_synthesis, [cv2.IMWRITE_JPEG_QUALITY, 100])