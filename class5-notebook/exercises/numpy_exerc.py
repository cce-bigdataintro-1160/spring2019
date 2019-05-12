#!/usr/bin/env python3

import numpy as np

# 1
myarray = np.array([1, 22.4, 5, 35, 4, 6.7, 3, 8, 40])

print(myarray.ndim)
print(myarray.shape)
print(myarray.size)
print(myarray.dtype)

# 2
mymatrix = np.array([['a', 'b'], ['c', 'd'], [3, 3]])

print(mymatrix.ndim)
print(mymatrix.shape)
print(mymatrix.size)
print(mymatrix.dtype)

# 3
array_arange = np.arange(3, 10)
array_linspace = np.linspace(3, 10)
array_rand = np.random.rand(1, 3)

print(array_arange)
print(array_linspace)
print(array_rand)

# 4
matrix_zeros = np.zeros((3, 3))
matrix_ones = np.ones((3, 3))
matrix_eye = np.eye(3)
matrix_rand = np.random.rand(3, 3)

print(matrix_zeros)
print(matrix_ones)
print(matrix_eye)
print(matrix_rand)

# 5
sevens_array = np.ones(20) * 7
reshaped_sevens = sevens_array.reshape(4, 5)
print(reshaped_sevens)

# 6
random_matrix = np.random.rand(6, 6)
print(random_matrix[0, 0])
print(random_matrix[0:2])
print(random_matrix[4:6])
print(random_matrix[2:4])
print(random_matrix[5:6])
print(random_matrix[2:4, 2:4])

for i in range(0, random_matrix[0].size):
    print(random_matrix[:, i].sum())
    print(random_matrix[:, i].mean())
    print(random_matrix[:, i].max())
    print(random_matrix[:, i].min())
