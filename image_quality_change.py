import numpy as np
import cv2
import math

filename = 'chroma_green.jpeg'

# 画像の読み込み
image = cv2.imread(filename)

# 画像の幅，高さ，bpp（チャンネル数）を取得
width = image.shape[1]
height = image.shape[0]
bpp = image.shape[2] * image.dtype.type(0).nbytes
imagesize = image.nbytes

arr = np.zeros((height, width, 3))
image_new = np.zeros([height, width, bpp], dtype=np.uint8)

for y in range(height):
  for x in range(width):
    arr[y, x, 0] = image[y, x, 0]
    arr[y, x, 1] = image[y, x, 1]
    arr[y, x, 2] = image[y, x, 2]

for y in range(height):
  for x in range(width):
    #print('y = ', y , 'x = ', x , arr[y][x])

    image_new [y,x,0] = arr[y, x, 0]
    image_new [y,x,1] = arr[y, x, 1]
    image_new [y,x,2] = arr[y, x, 2]

# 出力ファイル名
out_filename = 'image_new.png'

# 画像の保存
cv2.imwrite('chroma_green_q1.jpg', image_new, [cv2.IMWRITE_JPEG_QUALITY, 1])
cv2.imwrite('chroma_green_q5.jpg', image_new, [cv2.IMWRITE_JPEG_QUALITY, 5])
cv2.imwrite('chroma_green_q10.jpg', image_new, [cv2.IMWRITE_JPEG_QUALITY, 10])
cv2.imwrite('chroma_green_q20.jpg', image_new, [cv2.IMWRITE_JPEG_QUALITY, 20])
cv2.imwrite('chroma_green_q40.jpg', image_new, [cv2.IMWRITE_JPEG_QUALITY, 40])
cv2.imwrite('chroma_green_q80.jpg', image_new, [cv2.IMWRITE_JPEG_QUALITY, 80])