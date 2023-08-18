import numpy as np
import cv2
import math


# 画像の読み込み
#filename = 'q100_s.jpg'
filename = 'chroma_green.jpeg'
image = cv2.imread(filename)
# 画像タイプの変換
#image = image.astype(np.float64)

# 画像の幅，高さ，bpp（チャンネル数）を取得
width = image.shape[1]
height = image.shape[0]
bpp = image.shape[2] * image.dtype.type(0).nbytes
imagesize = image.nbytes


# 画像の読み込み
#filename = 'noise_s.jpg'
filename = 'chroma_green_q80.jpg'
image2 = cv2.imread(filename)
# 画像タイプの変換
#image2 = image2.astype(np.float64)


# 画像の幅，高さ，bpp（チャンネル数）を取得
width2 = image2.shape[1]
height2 = image2.shape[0]
bpp2 = image2.shape[2] * image2.dtype.type(0).nbytes
imagesize2 = image2.nbytes

# リストの作成
arr = np.zeros((height, width, 3))
image_ciexyz = np.zeros((height, width, 3))
image_ciexyz = np.zeros([height, width, bpp], dtype=np.uint8)
image_ciexyz_2 = np.zeros((height, width, 3))
image_ciexyz_2 = np.zeros([height, width, bpp], dtype=np.uint8)
image_cielab = np.zeros((height, width, 3))
image_cielab = np.zeros([height, width, bpp], dtype=np.float64)
image_cielab_2 = np.zeros((height, width, 3))
image_cielab_2 = np.zeros([height, width, bpp], dtype=np.float64)

def lab (k):
  if k > 0.008856:
    k = k**(1/3)
  else:
    k = 7.7871*k + 16/116
  return k

col_dif = 0
col_dif = np.uint16(0)
sum = np.uint16(0)

for y in range(height):
  for x in range(width):
    sum = np.uint16(0)

    image_ciexyz[y,x,0] = (image[y,x,0]/255)**(2.2) #B
    image_ciexyz[y,x,1] = (image[y,x,1]/255)**(2.2) #G
    image_ciexyz[y,x,2] = (image[y,x,2]/255)**(2.2) #R

    image_ciexyz[y,x,0] = 100 * (0.4124*image_ciexyz[y,x,2] + 0.3576*image_ciexyz[y,x,1] #X
                                 + 0.1805*image_ciexyz[y,x,0])
    image_ciexyz[y,x,1] = 100 * (0.2126*image_ciexyz[y,x,2] + 0.7152*image_ciexyz[y,x,1] #Y
                                 + 0.0722*image_ciexyz[y,x,0])
    image_ciexyz[y,x,2] = 100 * (0.0193*image_ciexyz[y,x,2] + 0.1192*image_ciexyz[y,x,1] #Z
                                 + 0.9504*image_ciexyz[y,x,0])

    image_cielab[y,x,0] = 116*lab( image_ciexyz[y,x,0] / 100.0) - 16 #L 
    image_cielab[y,x,1] = 500*( lab(image_ciexyz[y,x,0] / 95.05) - lab(image_ciexyz[y,x,1] /100.0) )  #a
    image_cielab[y,x,2] = 200*( lab(image_ciexyz[y,x,1] / 100.0) - lab(image_ciexyz[y,x,2] /108.89) ) #b


    
    image_ciexyz_2[y,x,0] = (image2[y,x,0]/255.0)**2.2 #B
    image_ciexyz_2[y,x,1] = (image2[y,x,1]/255.0)**2.2 #G
    image_ciexyz_2[y,x,2] = (image2[y,x,2]/255.0)**2.2 #R

    image_ciexyz_2[y,x,0] = 100 * (0.4124*image_ciexyz_2[y,x,2] + 0.3576*image_ciexyz_2[y,x,1]
                                 + 0.1805*image_ciexyz_2[y,x,0])  
    image_ciexyz_2[y,x,1] = 100 * (0.2126*image_ciexyz_2[y,x,2] + 0.7152*image_ciexyz_2[y,x,1]
                                 + 0.0722*image_ciexyz_2[y,x,0])
    image_ciexyz_2[y,x,2] = 100 * (0.0193*image_ciexyz_2[y,x,2] + 0.1192*image_ciexyz_2[y,x,1]
                                 + 0.9504*image_ciexyz_2[y,x,0])
    
    image_cielab_2[y,x,0] = 116*lab( image_ciexyz_2[y,x,0] /100.0) - 16
    image_cielab_2[y,x,1] = 500*(lab( image_ciexyz_2[y,x,0] /95.05) - lab( image_ciexyz_2[y,x,1] /100.0))
    image_cielab_2[y,x,2] = 200*(lab( image_ciexyz_2[y,x,1] /100.0) - lab( image_ciexyz_2[y,x,2] /108.89))
    

    sum += (image_cielab[y,x,0] - image_cielab_2[y,x,0])**2
    sum += (image_cielab[y,x,1] - image_cielab_2[y,x,1])**2
    sum += (image_cielab[y,x,2] - image_cielab_2[y,x,2])**2

    sum = math.sqrt(sum)

    col_dif += sum


print('filename2 = ', filename)
print('色差は: ', col_dif)
print("n = ", height*width)

col_dif /= (height*width)


# 課題3-5：画像1 と画像2 の色差*ΔE は 7.525（小数点第4 位で四捨五入）
print('色差は: ', col_dif)
