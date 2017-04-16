#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

sys.setrecursionlimit(1100)
#sys.maxint
#-sys.maxint-1

def paint(lake, i, j):
    if lake[i][j] != 'W':
        return

    lake[i][j] = 'X'
    paint(lake, i-1, j-1)
    paint(lake, i-1, j)
    paint(lake, i-1, j+1)
    paint(lake, i,   j-1)
    paint(lake, i,   j+1)
    paint(lake, i+1, j-1)
    paint(lake, i+1, j)
    paint(lake, i+1, j+1)

def solve(R, C, lake):
    answer = 0
    for i in range(1, R+1):
        for j in range(1, C+1):
            if lake[i][j] == 'W':
                answer += 1
                paint(lake, i, j)

    return answer


if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        (R, C) = map(int, f.readline().rstrip().split())
        lake = [['.' for c in range(C+2)] for r in range(R+2)]
        for j in range(R):
            row = list(f.readline().rstrip())
            for k in range(C):
                lake[j+1][k+1] = row[k]

        answer = solve(R, C, lake)

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

