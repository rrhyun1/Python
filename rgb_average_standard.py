import numpy as np
import cv2
import math


# 画像の読み込み
filename = 'green.jpeg'
image = cv2.imread(filename)

# 画像の幅，高さ，bpp（チャンネル数）を取得
width = image.shape[1]
height = image.shape[0]
bpp = image.shape[2] * image.dtype.type(0).nbytes
imagesize = image.nbytes

b_avg = 0
g_avg = 0
r_avg = 0
b_dev = 0
g_dev = 0
r_dev = 0

for y in range(height):
  for x in range(width):
  # B, G, Rの順番で並んでいるので注意してください
    b = image[y, x, 0]
    g = image[y, x, 1]
    r = image[y, x, 2]

    b_avg += b
    g_avg += g
    r_avg += r

b_avg /= (height*width)
g_avg /= (height*width)
r_avg /= (height*width)

print('R_avg:', r_avg, ' G_avg:', g_avg, ' B_avg: ', b_avg)

for y in range(height):
  for x in range(width):
    b = image[y, x, 0]
    g = image[y, x, 1]
    r = image[y, x, 2]

    b_dev += (b_avg-b)**2
    g_dev += (g_avg-g)**2
    r_dev += (r_avg-r)**2

b_stdv = math.sqrt(b_dev / (height*width))
g_stdv = math.sqrt(g_dev / (height*width))
r_stdv = math.sqrt(r_dev / (height*width))

print('R_stdv:', r_stdv, ' G_stdv:', g_stdv, ' B_stdv: ', b_stdv)