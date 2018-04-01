#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

sys.setrecursionlimit(1100)
#sys.maxint
#-sys.maxint-1

def solve(AC, AJ, ACs, AJs):
    print AC, AJ, ACs, AJs
    return 0


if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        (AC, AJ) = map(int, f.readline().rstrip().split())
        ACs = []
        for j in range(AC):
            ACs.append(map(int, f.readline().rstrip().split()))
        AJs = []
        for j in range(AJ):
            AJs.append(map(int, f.readline().rstrip().split()))

        answer = solve(AC, AJ, ACs, AJs)

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

