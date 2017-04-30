#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import math

sys.setrecursionlimit(1100)
#sys.maxint
#-sys.maxint-1

dp = {}

def dfs(cakes, i, K):
    global dp

    if (i, K) in dp:
        return dp[(i, K)]

    if K == 0:
        return 0

    if i >= len(cakes):
        return -sys.maxint-1

    # Use this
    a = dfs(cakes, i+1, K-1) + cakes[i][0]*cakes[i][1]*2 + (pow(cakes[i][0],2) if K == 1 else 0)

    # do not use
    a = max(dfs(cakes, i+1, K), a)

    dp[(1, K)] = a
    return a


def solve(N, K, cakes):
    global dp
    dp = {}
    a = dfs(cakes, 0, K)
    return a*math.pi


if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        (N, K) = map(int, f.readline().rstrip().split())
        cakes = []
        for j in range(N):
            cakes.append(map(int, f.readline().rstrip().split()))

        answer = solve(N, K, sorted(cakes, key=lambda x:x[0]))

        print "Case #%d: %f" % (i+1, answer)

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

