import numpy as np
import cv2
import math


# 画像の読み込み
filename = 'chroma_green.jpeg'
image = cv2.imread(filename)
# 画像タイプの変換
image = image.astype(np.float64)


# 画像の幅，高さ，bpp（チャンネル数）を取得
width = image.shape[1]
height = image.shape[0]
bpp = image.shape[2] * image.dtype.type(0).nbytes
imagesize = image.nbytes


# 画像の読み込み
filename = 'chroma_green_q1.jpeg'
image_q1 = cv2.imread(filename)
# 画像タイプの変換
image_q1 = image_q1.astype(np.float64)

# 画像の幅，高さ，bpp（チャンネル数）を取得
width_q1 = image_q1.shape[1]
height_q1 = image_q1.shape[0]
bpp_q1 = image_q1.shape[2] * image_q1.dtype.type(0).nbytes
imagesize_q1 = image_q1.nbytes


arr = np.zeros((height, width, 3))
image_new = np.zeros([height, width, bpp], dtype=np.uint8)

mse = 0

for y in range(height):
  for x in range(width):
    mse += (image[y, x, 0] - image_q1[y, x, 0])**2
    mse += (image[y, x, 1] - image_q1[y, x, 1])**2
    mse += (image[y, x, 2] - image_q1[y, x, 2])**2

mse /= (3*height*width)

print('MSE = ', mse)

PSNR = 10 * math.log10(255**2/mse)

print('PSNR = ', PSNR)


def psnr (image1):
  mse = 0

  for y in range(height):
    for x in range(width):
      mse += (image[y, x, 0] - image1[y, x, 0])**2
      mse += (image[y, x, 1] - image1[y, x, 1])**2
      mse += (image[y, x, 2] - image1[y, x, 2])**2

  mse /= (3*height*width)
  PSNR = 10 * math.log10(255**2/mse)
  return PSNR

print(psnr(image_q1))

