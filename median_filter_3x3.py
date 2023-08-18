import numpy as np
import cv2

in_filename = 'q100_s.jpg'
out_filename = 'q100_s_median_5.jpg'
data = cv2.imread(in_filename)

width = data.shape[1]
height = data.shape[0]
bpp = data.shape[2]


# メモリ確保
median_data = np.zeros([height, width, bpp])

for h in range(2, height-2):
  for w in range(2, width-2):

    pixel_value_b = [0]*25
    pixel_value_g = [0]*25
    pixel_value_r = [0]*25

    for y in range(5):
      for x in range(5):
        pixel_value_b[5*y + x] = data[h+y-2, w+x-2, 0]
        pixel_value_g[5*y + x] = data[h+y-2, w+x-2, 1]
        pixel_value_r[5*y + x] = data[h+y-2, w+x-2, 2]

        if h==10 and w ==10 and y == 1 and x ==1:
          print('ソート前')
          print(f'h = {h} w = {w} y = {y} x = {x}')
          print(pixel_value_r)

    pixel_value_b.sort()
    pixel_value_g.sort()
    pixel_value_r.sort()

    median_data[h, w, 0] = pixel_value_b[12]
    median_data[h, w, 1] = pixel_value_g[12]
    median_data[h, w, 2] = pixel_value_r[12]

    if h==10 and w ==10:
      print('ソート後')
      print(f'h = {h} w = {w} y = {y} x = {x}')
      print(pixel_value_r)
      print('median_data[h+1, w+1, 2]:', median_data[h, w, 2])

for h in range(0, height):
  for w in range(0, width):
    for b in range(bpp):
      if (h==0 or h==1 or h==height-1 or h==height-2
          or w ==0 or w==1 or w==width-2 or w==width-1 ):
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

