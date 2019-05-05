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
    for value in line_values:
        try:
            corrected_line.append(int(value))
        except:
            corrected_line.append(float(value))
    corrected_file.append(corrected_line)

corrected_file=corrected_file[0:2]

transposed_list=[]
for column in corrected_file[0]:
    transposed_list.append([])

for line in corrected_file:
    for idx, column in enumerate(line):
        transposed_list[idx].append(column)

print(transposed_list)
file.close()
