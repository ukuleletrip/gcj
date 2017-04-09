#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

MAX_TIME = 1000000000*25

def min_to_n(mins, Ms):
    n = 0
    rs = []
    for i in range(len(Ms)):
        n += mins/Ms[i]
        rs.append(mins%Ms[i])

    return n, rs

def solve(n, N, rs):
    while True:
        max_idx = rs.index(max(rs))
        n += 1
        if n == N:
            return max_idx+1
        rs[max_idx] = -1
    print 'kuso'
    return 0
        

def solveit(B, N, Ms):
    start = 0
    end = MAX_TIME/2
    while end > start:
        (n, rs) = min_to_n((start+end)/2, Ms)
        if n < N and N <= n+B:
            # this is it !!
            return solve(n, N, rs)
        if n < N:
            start = (start+end)/2+1
        else:
            end = (start+end)/2-1


    print 'kuso1'
    return 0

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        (B, N) = map(int, f.readline().rstrip().split())
        Ms = map(int, f.readline().rstrip().split())
        answer = solveit(B, N, Ms)

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

