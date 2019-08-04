#!/usr/bin/env python

import os

file_path = 'housing.data'

if os.path.isfile(file_path):
    print('I have a valid file!!!')
else:
    print('Invalid file, I\'ll crash')

file = open('housing.data')

corrected_file = []
for line in file.readlines():
    clean_line = line.replace('  ', ' ').replace('  ', ' ').strip()
    line_values = clean_line.split(' ')
    corrected_line = []
    print(line_values)
    for value in line_values:
        # for homework:
        # identify what type of data each value is, and cast it
        # to the appropriate type, then print the new, properly-typed
        # list to the screen.
        # I.e. ['0.04741', '0.00', '11.930', '0', '0.5730', '6.0300', '80.80', '2.5050', '1', '273.0', '21.00', '396.90', '7.88', '11.90']
        # becomes: [0.04741, 0.0, 11.93, 0, 0.573, 6.03, 80.8, 2.505, 1, 273.0, 21.0, 396.90, 7.88, 11.90]
    print(corrected_line)
print(corrected_file)

file.close()
