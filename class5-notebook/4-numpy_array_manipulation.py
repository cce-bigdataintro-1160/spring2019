#!/usr/bin/env python3

import numpy as np


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')


random_int_array = np.random.randint(1, 100, 30)

# Arrays Information
pretty_print('array shape', random_int_array.shape)
pretty_print('array type', random_int_array.dtype)

# Slicing Arrays
pretty_print('random_int_array', random_int_array)
pretty_print('slice_array1', random_int_array[4:14])
pretty_print('slice_array2', random_int_array[4:14:2])
pretty_print('slice_array3', random_int_array[:])
pretty_print('slice_array4', random_int_array[5:-5])

# Reshaping Arrays
reshaped_random_int_matrix = random_int_array.reshape(5, 6)

pretty_print('matrix shape', reshaped_random_int_matrix.shape)
pretty_print('matrix type', reshaped_random_int_matrix.dtype)

pretty_print('reshaped_random_int_matrix', reshaped_random_int_matrix)
pretty_print('slice_matrix1', reshaped_random_int_matrix[1:3, 3:5])
pretty_print('slice_matrix2', reshaped_random_int_matrix[0:3, :])
pretty_print('slice_matrix3', reshaped_random_int_matrix[:, 2:3])


# Filtering arrays by a condition
pretty_print('filtered_matrix', reshaped_random_int_matrix[reshaped_random_int_matrix > 10])

# Multiplying arrays
pretty_print('multiplied_matrix', reshaped_random_int_matrix * 2)