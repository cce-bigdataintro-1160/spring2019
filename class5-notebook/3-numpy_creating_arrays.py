#!/usr/bin/env python3

import numpy as np


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')


pretty_print('simple_array', np.array([1, 2]))

pretty_print('matrix', np.array([[1, 2], [1, 4], [1, 3]]))

pretty_print('range_array', np.arange(1, 15))

pretty_print('zeros_array', np.zeros(10))

pretty_print('zeros_matrix', np.zeros((5, 5)))

pretty_print('ones_matrix', np.ones((5, 5)))

pretty_print('sevens_matrix', np.ones((5, 5)) * 7)

pretty_print('random_array', np.random.rand(5))

pretty_print('random_matrix', np.random.rand(4, 4))

random_int_array = np.random.randint(1, 100, 20)
pretty_print('random_int_array', random_int_array)

pretty_print('reshaped_random_int_matrix', random_int_array.reshape(5, 4))

pretty_print('identity_matrix', np.eye(4))

pretty_print('linspace_array', np.linspace(0, 20, 10))
