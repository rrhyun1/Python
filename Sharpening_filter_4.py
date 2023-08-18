import numpy as np
import cv2

in_filename = 'chroma_green.jpeg'
out_filename = 'chroma_green_sharpening_filter_8.jpg'
data = cv2.imread(in_filename)

width = data.shape[1]
height = data.shape[0]
bpp = data.shape[2]

# メモリ確保
out_data = np.zeros([height, width, bpp])

# 平均値フィルタ用のカーネル
kernel = [
    [-1, -1, -1],
    [-1, 9, -1],
    [-1, -1, -1]
]
print('width= ' + str(width) + ', height = '+ str(height) + ', bpp = ' + str(bpp) )

for h in range(height):
  for w in range(width):
    for b in range(bpp):
      # 要素数９の配列を確保
      pixel_value = [0]*9

      sum = 0.0
      for i in range(3):
        for j in range(3):
          px = w + j - 1
          py = h + i - 1

          # はみ出した場合の例外処理
          if((px < 0) or (py < 0)): continue
          if((px >= width) or (py >= height)): continue

          I = data[py, px, b]
          g = kernel[j][i]

          sum += I * g

      out_data[h, w, b] = sum

# 画像データをファイルとして保存
cv2.imwrite(out_filename, out_data)


x = 0
y = 100

for i in range(10):
  b = out_data[y, x+i, 0]
  g = out_data[y, x+i, 1]
  r = out_data[y, x+i, 2]

  print('y = ', y ,'x = ', x+i ,' R:', r, ' G:', g, ' B: ', b)