# Matrix Algebra

import numpy as np

A = np.array([[1, 2, 3], [2, 7, 4]])
B = np.array([[1, -1], [0, 1]])
C = np.array([[5, -1], [9, 1], [6, 0]])
D = np.array([[3, -2, -1], [1, 2, 3]])
u = np.array([6, 2, -3, 5])
v = np.array([3, 5, -1, 4])
w = np.array([[1], [8], [0], [5]])


# 1. Matrix Dimensions
A.shape # (2, 3)

B.shape # (2, 2)

C.shape # (3, 2)

D.shape # (2, 3)

u.shape
np.matrix([6, 2, -3, 5]).shape # (1, 4)

w.shape # (4, 1)


# 2. Vector Operations
u+v # array([ 9,  7, -4,  9])

u-v # array([ 3, -3, -2,  1])

6*u # array([ 36,  12, -18,  30])

u*v # array([18, 10,  3, 20])

np.linalg.norm(u) # magnitude of u = 8.6023252670426267


# 3. Matrix Operations
A + C # not defined

A - C.T
# array([[-4, -7, -3],
       # [ 3,  6,  4]])

C.T + 3*D
# array([[14,  3,  3],
       # [ 2,  7,  9]])

B*A # undefined

B*A.T # undefined
