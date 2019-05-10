#!/usr/bin/env python3

import numpy as np


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')


random_int_array = np.random.randint(1, 100, 20)

pretty_print('random_int_array', random_int_array)

pretty_print('np.mean(random_int_array)', np.mean(random_int_array))
pretty_print('np.min(random_int_array)', np.min(random_int_array))
pretty_print('np.max(random_int_array)', np.max(random_int_array))
pretty_print('np.std(random_int_array)', np.std(random_int_array))

pretty_print('np.mean(random_int_array)', random_int_array.mean())
pretty_print('np.min(random_int_array)', random_int_array.min())
pretty_print('np.max(random_int_array)', random_int_array.max())
pretty_print('np.std(random_int_array)', random_int_array.std())

reshaped_random_int_matrix = random_int_array.reshape(5, 4)

pretty_print('np.mean(reshaped_random_int_matrix)', np.mean(reshaped_random_int_matrix))
pretty_print('np.min(reshaped_random_int_matrix)', np.min(reshaped_random_int_matrix))
pretty_print('np.max(reshaped_random_int_matrix)', np.max(reshaped_random_int_matrix))
pretty_print('np.std(reshaped_random_int_matrix)', np.std(reshaped_random_int_matrix))

pretty_print('np.mean(reshaped_random_int_matrix)', np.mean(reshaped_random_int_matrix[1]))
pretty_print('np.min(reshaped_random_int_matrix)', np.min(reshaped_random_int_matrix[1]))
pretty_print('np.max(reshaped_random_int_matrix)', np.max(reshaped_random_int_matrix[1]))
pretty_print('np.std(reshaped_random_int_matrix)', np.std(reshaped_random_int_matrix[1]))
