import sys

# to read script arguments use sys.argv[1]
# to read user inputs use myinput=input('Please write your name')

for item in range(0,100):
  if (item % 10 == 0):
    print(item)
  elif (item % 11 == 0):
    print(f'{item} is div by 11')
  else:
    print('nah')

