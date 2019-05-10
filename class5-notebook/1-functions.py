#!/usr/bin/env python3

import os


def pretty_print(a):
    return f"My value is: {a}"


def sum_one(a):
    return a + 1


def sum(a, b):
    return a + b


def prefix_string_with(prefix, string):
    return f'{prefix}{string}'


def check(prefix, string):
    return f'{prefix}{string}'


def reverse(s):
    return s[::-1]


def isPalindrome(s):
    if s == reverse(s):
        return True
    else:
        return False


def print_file(file_path):
    if os.path.isfile(file_path):
        print(f'{file_path} is valid, printing file')
        for l in open(file_path).readlines():
            print(l)
    else:
        print(f'cannot print file, {file_path} doesn\'t have a valid file')
