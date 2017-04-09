#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

sys.setrecursionlimit(1100)
#sys.maxint
#-sys.maxint-1

def findit(A, limit):
    foundnum = {}
    found = 0
    sA = str(A)
    for i in range(1, len(sA)):
        newA = int(sA[i:] + sA[:i])
        if newA > A and newA <= limit and not newA in foundnum:
            foundnum[newA] = 1
            found += 1
            #print "found %d %d" % (A, newA)
    return found

def solveit(A, B):
    answer = 0
    N = A
    while N <= B:
        answer += findit(N, B)
        N += 1
    return answer

if __name__ == '__main__':
    f = open(sys.argv[1])
    num_of_case = int(f.readline())
    for i in range(num_of_case):
        nums = map(int, f.readline().rstrip().split())
        answer = solveit(nums[0], nums[1])
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

