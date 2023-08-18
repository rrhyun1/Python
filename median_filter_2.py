import numpy as np
import cv2

in_filename = 'q100_s.jpg'
out_filename = 'q100_s_median_3-2.jpg'
data = cv2.imread(in_filename)

width = data.shape[1]
height = data.shape[0]
bpp = data.shape[2]


# メモリ確保
median_data = np.zeros([height, width, bpp])

for h in range(1, height-1):
  for w in range(1, width-1):
    pixel_value_b = [0]*9
    pixel_value_g = [0]*9
    pixel_value_r = [0]*9

    for y in range(3):
      for x in range(3):
        pixel_value_b[3*y + x] = data[h+y-1, w+x-1, 0]
        pixel_value_g[3*y + x] = data[h+y-1, w+x-1, 1]
        pixel_value_r[3*y + x] = data[h+y-1, w+x-1, 2]

        if h==10 and w ==10 and y == 1 and x ==1:
          print('ソート前')
          print(f'h = {h} w = {w} y = {y} x = {x}')
          print(pixel_value_r)

    pixel_value_b.sort()
    pixel_value_g.sort()
    pixel_value_r.sort()

    for y in range(3):
      for x in range(3):
        median_data[h+y-1, w+x-1, 0] = pixel_value_b[3*y + x]
        median_data[h+y-1, w+x-1, 1] = pixel_value_g[3*y + x]
        median_data[h+y-1, w+x-1, 2] = pixel_value_r[3*y + x]

        if h==10 and w ==10 and y == 1 and x ==1:
          print('ソート後')
          print(f'h = {h} w = {w} y = {y} x = {x}')
          print(pixel_value_r)

for h in range(0, height):
  for w in range(0, width):
    for b in range(bpp):
      if h == 0 or h == height-1 or w ==0 or w==width-1:
        median_data[h, w, b] = data[h,w,b]

# メモリ確保
out_data = np.zeros([height, width, bpp])

for h in range(height):
  for w in range(width):
    out_data[h, w, 0] = median_data[h, w, 0]
    out_data[h, w, 1] = median_data[h, w, 1]
    out_data[h, w, 2] = median_data[h, w, 2]


# 画像データをファイルとして保存
cv2.imwrite(out_filename, out_data)
