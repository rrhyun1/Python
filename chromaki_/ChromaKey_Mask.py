import numpy as np
import cv2
from google.colab.patches import cv2_imshow
import math


filename = 'green.jpeg'

# 画像の読み込み
image = cv2.imread(filename)

# 画像の幅，高さ，bpp（チャンネル数）を取得
width = image.shape[1]
height = image.shape[0]
bpp = image.shape[2] * image.dtype.type(0).nbytes
imagesize = image.nbytes



#マスク画像の作成
image_mask = np.zeros([height, width, bpp], dtype=np.uint8)

for y in range(height):
  for x in range(width):
    image_mask[y, x, 0] = 255
    image_mask[y, x, 1] = 255
    image_mask[y, x, 2] = 255



filename2 = 'chroma_green.jpeg'

# 画像の読み込み
image2 = cv2.imread(filename2)

# 画像の幅，高さ，bpp（チャンネル数）を取得
width2 = image2.shape[1]
height2 = image2.shape[0]
bpp2 = image2.shape[2] * image2.dtype.type(0).nbytes
imagesize2 = image2.nbytes


# 画素の判別
# R_avg: 95.56548849285085  G_avg: 174.46280319612413  B_avg:  82.95203443549488
b_avg = 0
g_avg = 0
r_avg = 0

for y in range(height):
  for x in range(width):

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



'''d = 51'''

d = 51
for y in range(height):
  for x in range(width):
    if ( (g_avg-d <= image2[y, x, 1] <= g_avg+d) and 
     (b_avg-d <= image2[y, x, 0] <= b_avg+d) and 
      (r_avg-d <= image2[y, x, 2] <= r_avg+d)): 
      image_mask[y, x, 0] = 0
      image_mask[y, x, 1] = 0
      image_mask[y, x, 2] = 0

# R: 13  G: 33  B:  8 
#b = image[y, x, 0]
#g = image[y, x, 1]
#r = image[y, x, 2]

for y in range(height):
  for x in range(width):
    if ( (0 <= image2[y, x, 0] <= 20) and 
     (25 <= image2[y, x, 1] <= 40) and 
      (5 <= image2[y, x, 2] <= 30)): 
      image_mask[y, x, 0] = 0
      image_mask[y, x, 1] = 0
      image_mask[y, x, 2] = 0


# 画像の保存
cv2.imwrite('result2-2-50-1.jpg', image_mask, [cv2.IMWRITE_JPEG_QUALITY, 100])

