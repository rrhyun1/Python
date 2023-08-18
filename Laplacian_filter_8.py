import numpy as np
import cv2

in_filename = 'chroma_green.jpeg'
out_filename = 'chroma_green_Laplacian_filter_8.jpg'
data = cv2.imread(in_filename)

width = data.shape[1]
height = data.shape[0]
bpp = data.shape[2]

# メモリ確保
filter_x = np.zeros([height, width, bpp])
filter_y = np.zeros([height, width, bpp])
filter_z = np.zeros([height, width, bpp])
filter_r = np.zeros([height, width, bpp])
filter = np.zeros([height, width, bpp])

for h in range(2, height-2):
  for w in range(2, width-2):
    for b in range(bpp):
        filter_x[h, w, b] = data[h, w-1, b] -2 * data[h, w, b] + data[h, w+1, b]
        filter_y[h, w, b] = data[h-1, w, b] -2 * data[h, w, b] + data[h+1, w, b]
        filter_z[h, w, b] = data[h-1, w-1, b] -2 * data[h, w, b] + data[h+1, w+1, b]
        filter_r[h, w, b] = data[h-1, w+1, b] -2 * data[h, w, b] + data[h+1, w-1, b]
        filter[h, w, b] = filter_x[h, w, b] + filter_y[h, w, b] + filter_z[h, w, b] + filter_r[h, w, b]

# メモリ確保
out_data = np.zeros([height, width, bpp])

for h in range(height):
  for w in range(width):
    for b in range(bpp):
        out_data[h, w, b] = data[h, w, b] - filter[h, w, b]


# 画像データをファイルとして保存
cv2.imwrite(out_filename, out_data)