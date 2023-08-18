import numpy as np
import cv2
from google.colab.patches import cv2_imshow
import math


# クロマキー画像の読み込み
filename = 'green.jpeg'
image = cv2.imread(filename)

# 画像の幅，高さ，bpp（チャンネル数）を取得
width = image.shape[1]
height = image.shape[0]
bpp = image.shape[2] * image.dtype.type(0).nbytes
imagesize = image.nbytes



# マスク画像の読み込み
filename = 'result2-2-51-1.jpg'
image_mask = cv2.imread(filename)

# 画像の幅，高さ，bpp（チャンネル数）を取得
width_mask = image_mask.shape[1]
height_mask = image_mask.shape[0]
bpp_mask = image_mask.shape[2] * image_mask.dtype.type(0).nbytes
imagesize_mask = image_mask.nbytes




# 背景画像の読み込み
filename = 'background.jpeg'
image_bg = cv2.imread(filename)

# 画像の幅，高さ，bpp（チャンネル数）を取得
width_bg = image_bg.shape[1]
height_bg = image_bg.shape[0]
bpp_bg = image_bg.shape[2] * image_bg.dtype.type(0).nbytes
imagesize_bg = image_bg.nbytes



#クロマキー合成画像の作成
image_chroma = np.zeros([height, width, bpp], dtype=np.uint8)

for y in range(height):
  for x in range(width):
    if image_mask[y, x, 0] == 0:
      image_chroma[y, x, 0] = image_bg[y, x, 0]
      image_chroma[y, x, 1] = image_bg[y, x, 1]
      image_chroma[y, x, 2] = image_bg[y, x, 2]



# 人物画像の読み込み
filename2 = 'chroma_green.jpeg'
image2 = cv2.imread(filename2)

# 画像の幅，高さ，bpp（チャンネル数）を取得
width2 = image2.shape[1]
height2 = image2.shape[0]
bpp2 = image2.shape[2] * image2.dtype.type(0).nbytes
imagesize2 = image2.nbytes


for y in range(height2):
  for x in range(width2):
    if image_mask[y, x, 0] == 255:
      image_chroma[y, x, 0] = image2[y, x, 0]
      image_chroma[y, x, 1] = image2[y, x, 1]
      image_chroma[y, x, 2] = image2[y, x, 2]


# 画像の保存
cv2.imwrite('result2-3.jpg', image_chroma, [cv2.IMWRITE_JPEG_QUALITY, 100])