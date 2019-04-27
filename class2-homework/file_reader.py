import os


#if os.path.isfile('./fdgdfhidden_file/wine.data'):
#  print('yey it\'s a file')
#else: 
#  print('booh no file for me:')

file=open('./hidden_file/wine.data')

for line in file.readlines():
    print(line)
