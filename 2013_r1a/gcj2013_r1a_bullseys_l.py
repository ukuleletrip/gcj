#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys


def doit(r, t):
    max_ans = 200000000000000000
    answer = 0

    right = t
    left = 0
    while left <= right:
        mid = (left+right)/2
        if t < mid*(2*r+2*mid-1):
            right = mid-1
        else:
            left = mid+1
            answer = mid

    return answer

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        (r, t) = map(int, f.readline().rstrip().split())
        answer = doit(r, t)
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

