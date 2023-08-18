import numpy as np

A = np.array([[2.0, 3.0, -1.0], [1.0, -1.0, 3.0],
               [1.0, 4.0, -4.0]])
b = np.array([2, 1, 4])

A_inv = np.linalg.pinv(A)
x = np.dot(A_inv, b)

print(x)

print(A_inv[0][0]*x[0] + A_inv[0][1]*x[1] + A_inv[0][2]*x[2])