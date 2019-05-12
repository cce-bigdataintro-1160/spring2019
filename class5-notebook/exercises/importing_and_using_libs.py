#!/usr/bin/env python3

import argparse
parser = argparse.ArgumentParser(description='Process some integer.')
parser.add_argument('myinteger', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
args = parser.parse_args()
print(args.myinteger)

import sys
print(sys.argv[1])

import os
print(os.path.isfile('./asdkfjoasdifoiadfj/titanic.zip'))

import time
print('before sleep')
time.sleep(3)
print('after sleep')

import random
print(random.randint(3, 10))

for i in range(0, 10):
    print(random.randint(0, 50))
    time.sleep(1)
