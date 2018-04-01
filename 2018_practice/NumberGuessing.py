#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

def solve(f, a, b, n):
    while True:
        if b <= a+1:
            guess = b
        else:
            guess = int((a+b)/2)+1
        print(guess, file=sys.stdout)
        sys.stdout.flush()
        answer = f.readline().rstrip()
        if answer == 'CORRECT':
            break
        elif answer == 'TOO_BIG':
            b = guess-1
        elif answer == 'TOO_SMALL':
            a = guess+1


if __name__ == '__main__':
    f = sys.stdin

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        (a, b) = map(int, f.readline().rstrip().split())
        n = int(f.readline())
        solve(f, a, b, n)


