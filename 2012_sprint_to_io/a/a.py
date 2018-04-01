#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

sys.setrecursionlimit(1100)
#sys.maxint
#-sys.maxint-1

def solveit(L, M, Ks):
    max_k = max(Ks)
    if L < max_k:
        return -1
    return L*M-(L-max(Ks))

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        param = map(int, f.readline().rstrip().split())
        L = param[0]
        M = param[1]
        Ks = param[2:]
        answer = solveit(L, M, Ks)
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

