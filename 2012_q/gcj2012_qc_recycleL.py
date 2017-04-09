#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys
#import table

sys.setrecursionlimit(1100)
#sys.maxint
#-sys.maxint-1

# this table was made by create_recycle_table()

recycle_table = {}

def create_recycle_table():
    A = 1
    limit = 2000000
    while A <= limit:
        digits = len(str(A))
        recycle_table[A] = []
        foundnum = {}
        n = 10
        for i in range(1, digits):
            newA = (A%n)*(10**(digits-i))+A/n
            if newA  > A and newA <= limit and not newA in foundnum:
                foundnum[newA] = 1
                recycle_table[A].append(newA)
            n *= 10
        A += 1
    #print recycle_table

def findit(A, limit):
    found = 0
    for num in recycle_table[A]:
        if num <= limit:
            found += 1
    return found

def solveit(A, B):
    answer = 0
    N = A
    while N <= B:
        answer += findit(N, B)
        N += 1
    return answer

if __name__ == '__main__':
    create_recycle_table()
    #exit(1)

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

