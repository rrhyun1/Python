import numpy as np
import matplotlib.pyplot as plt
import time

start_time = time.time()

"""
x = [23,8,34,12,42,6,1]
y = [39,44,36,30,37,35,15]
"""
x = [23,8,34,12,42,6,1,12,4,13,23,7,11,6,28,20,
     3,4,3,0,19,3,8,20,2,20,16,24,9,5,30,2,21,22,3,11,14]
y = [39,44,36,30,37,35,15,25,39,42,13,39,5,44,45,7,
     16,19,39,2,21,43,34,39,50,26,36,30,40,22,35,0,36,28,33,36,34]

# 2つの点間の距離を計算
def compute_distance(i, j):
    result = np.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)
    return result

# 点間の距離を保存する配列生成
distance_points = np.zeros((len(x), len(x)))

for i in range(len(x)):
    for j in range(len(x)):
        #自分自身との距離は大きい数にして最小値にならないようにする
        if (i == j):
            distance_points[i,j] = 1000.0
        else:
            distance_points[i,j] = compute_distance(i, j)

print('distance_points = \n',distance_points, end='\n\n')

#経路の配列
course = np.zeros(len(x)+2)
#経路の0目の要素は0
course[0] = 0
#累積距離
accumulate_distance = 0.0

#各点から最小の距離にある点の番地を保存する配列生成
index = np.zeros(len(x))

#視点を0番地の点にして、最小距離にある点を
#インデックス配列と経路配列に保存する
index[0] = np.argmin(distance_points[0])
course[1] = int(index[0])
accumulate_distance += compute_distance(0, int(index[0]))
print("index[0] = ",index[0], end='\n\n')

#一度通った点のインデックスの列は1000.0に初期化して
#最小値にならないようにす
distance_points[:, 0] = 1000.0

#for文を使って計算を繰り返す
for i in range(len(x)-1):
    index[i+1] = np.argmin(distance_points[int(index[i])])
    course[i+2] = int(index[i+1])
    accumulate_distance += compute_distance(i+1, int(index[i+1]))
    print("index[",i+1,"] = ",index[i+1], end='\n\n')
    distance_points[:, int(index[i])] = 1000.0

print(distance_points, end='\n\n')

#経路配列の最後のところは0にする（帰着するように）
course[len(x)] = 0

#経路配列を整数化する
course = course.astype(int)
print("経路：", course)


end_time = time.time()
print ("\n\ntime: ", end_time - start_time)
print("accumulate_distance :",accumulate_distance)



#グラフを描いて可視化する
for i in range(len(course)-1):
    plt.plot([x[course[i]], x[course[i+1]]], 
             [y[course[i]], y[course[i+1]]], 'r-')

for i in range(len(x)):
    plt.scatter(x[i], y[i])
    plt.text(x[i], y[i], str(i), verticalalignment='bottom', horizontalalignment='right')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of Points and Route')
plt.show()

