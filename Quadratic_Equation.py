import numpy as np
import math


x = [3,5,7]
y = np.roots(x)

print('np.roots: ',y)


#二次方程式の解の求め方
#ax^2 + bx +c = 0
a = 3 
b = 5 
c = 7
method = b**2 -4*a*c

if method < 0:
    method = -method

real = -b / (2*a)
imag = math.sqrt(method) / (a*2)

value1 = complex(real, imag)
value2 = complex(real, -imag)

print('解の公式: ',value1, value2)

print('差: ', y[0] - value1, y[1] - value2)