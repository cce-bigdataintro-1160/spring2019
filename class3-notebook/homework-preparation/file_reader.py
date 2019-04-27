import os


#if os.path.isfile('./fdgdfhidden_file/wine.data'):
#  print('yey it\'s a file')
#else: 
#  print('booh no file for me:')

file=open('./housing.data')

for line in file.readlines():
    replaced_line=line.strip().replace('  ',' ').replace('  ',' ')
    split_line=replaced_line.split(' ')
    #print(split_line)
    rebuilt_line=[]
    for value in split_line:
       rebuilt_line.append(float(value))
    print(rebuilt_line)


