#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import math

MAX_DIGITS = 18

def adjust_to_tidy(n):
    tidy = 0
    div = pow(10, MAX_DIGITS)
    prev = 0
    while True:
        now = n / div
        n %= div
        if now < prev:
            # broken point !!
            tidy += (prev-1) * div * 10
            while div:
                tidy += 9 * div
                div /= 10
            return tidy
        
        tidy += prev * div * 10
        div /= 10
        if div == 0:
            tidy += now
            break
        prev = now

    return tidy

def is_tidy(n):
    prev = 10
    while n > 0:
        now = n % 10
        if now > prev:
            return False
        n /= 10
        prev = now
    return True


def solve(N):
    n_in = N
    while True:
        n_out = adjust_to_tidy(n_in)
        if n_out == n_in:
            break
        n_in = n_out
    return n_out

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        N = int(f.readline())
        answer = solve(N)

        print "Case #%d: %d" % (i+1, answer)

# sort by key
# for k,v in sorted(d.items())
# sort by value
# for k,v in sorted(d.items(), key=lambda x:x[1])
# items() return tapple, tapple[0] is k, tapple[1] is v
#
# import copy
# copy.copy()
# copy.deepcopy()
#
# a = [0]*100
#
# for tc in xrange(1, int(sys.stdin.readline())+1):
#   A, B = [int(w) for w in sys.stdin.readline().split()]
#   p = [float(w) for w in sys.stdin.readline().split()]
#
# array = [[0 for j in range(m)] for i in range(n)]

